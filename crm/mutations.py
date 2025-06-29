import re
import graphene
from django.db import transaction
from .models import Customer, Product, Order
from .types import CustomerType, ProductType, OrderType

def is_valid_phone(phone):
    return re.match(r'^(\+\d{10,15}|\d{3}-\d{3}-\d{4})$', phone)

# --- 1. CreateCustomer ---
class CreateCustomer(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        phone = graphene.String()

    customer = graphene.Field(CustomerType)
    message = graphene.String()

    def mutate(self, info, name, email, phone=None):
        if Customer.objects.filter(email=email).exists():
            raise Exception("Email already exists")
        if phone and not is_valid_phone(phone):
            raise Exception("Invalid phone format")
        customer = Customer.objects.create(name=name, email=email, phone=phone or "")
        return CreateCustomer(customer=customer, message="Customer created successfully.")

# --- 2. BulkCreateCustomers ---
class BulkCreateCustomers(graphene.Mutation):
    class Arguments:
        input = graphene.List(
            graphene.InputObjectType(
                "CustomerInput",
                name=graphene.String(required=True),
                email=graphene.String(required=True),
                phone=graphene.String()
            )
        )

    customers = graphene.List(CustomerType)
    errors = graphene.List(graphene.String)

    def mutate(self, info, input):
        created = []
        errors = []

        with transaction.atomic():
            for idx, data in enumerate(input):
                try:
                    if Customer.objects.filter(email=data.email).exists():
                        raise Exception(f"Row {idx + 1}: Email already exists")
                    if data.phone and not is_valid_phone(data.phone):
                        raise Exception(f"Row {idx + 1}: Invalid phone format")
                    customer = Customer.objects.create(
                        name=data.name, email=data.email, phone=data.phone or ""
                    )
                    created.append(customer)
                except Exception as e:
                    errors.append(str(e))
        return BulkCreateCustomers(customers=created, errors=errors)

# --- 3. CreateProduct ---
class CreateProduct(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        price = graphene.Float(required=True)
        stock = graphene.Int(required=False)

    product = graphene.Field(ProductType)

    def mutate(self, info, name, price, stock=0):
        if price <= 0:
            raise Exception("Price must be positive")
        if stock < 0:
            raise Exception("Stock cannot be negative")
        product = Product.objects.create(name=name, price=price, stock=stock)
        return CreateProduct(product=product)

# --- 4. CreateOrder ---
class CreateOrder(graphene.Mutation):
    class Arguments:
        customer_id = graphene.ID(required=True)
        product_ids = graphene.List(graphene.ID, required=True)

    order = graphene.Field(OrderType)

    def mutate(self, info, customer_id, product_ids):
        from django.utils.timezone import now
        try:
            customer = Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            raise Exception("Invalid customer ID")

        products = Product.objects.filter(id__in=product_ids)
        if not products.exists():
            raise Exception("At least one valid product is required")

        total = sum([p.price for p in products])
        order = Order.objects.create(customer=customer, total_amount=total, order_date=now())
        order.products.set(products)
        return CreateOrder(order=order)
