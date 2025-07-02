# crm/models.py
from django.db import models
from django.core.exceptions import ValidationError
import re

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.phone and not re.match(r"^\+?\d[\d\s\-()]{7,20}$", self.phone):
            raise ValidationError({'phone': "Invalid phone number format."})
        if Customer.objects.filter(email=self.email).exclude(pk=self.pk).exists():
            raise ValidationError({'email': "Email already exists."})

    def save(self, *args, **kwargs):
        self.full_clean()  # Run validation
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)

    def clean(self):
        if self.price <= 0:
            raise ValidationError({'price': "Price must be positive."})
        if self.stock < 0:
            raise ValidationError({'stock': "Stock cannot be negative."})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField(Product)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def update_total_amount(self):
        if self.pk:
            self.total_amount = sum(product.price for product in self.products.all())
        else:
            self.total_amount = 0
        return self.total_amount

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.total_amount or self.total_amount != self.update_total_amount():
            self.total_amount = self.update_total_amount()
            super().save(update_fields=['total_amount'])

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"
