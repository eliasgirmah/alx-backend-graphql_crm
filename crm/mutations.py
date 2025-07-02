import re
import graphene
from django.db import transaction
from django.utils.timezone import now
from django.utils.dateparse import parse_datetime
from .models import Customer, Product, Order
from .types import CustomerType, ProductType, OrderType

# Helper validation function
def is_valid_phone(phone):
    return re.match(r'^(\+\d{10,15}|\d{3}-\d{3}-\d{4})$', phone)

# --- Input Types ---
class CustomerInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    email = graphene.String(required=True)
    phone = graphene.String()

class ProductInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    price = graphene.Float(required=True)
    stock = graphene.Int()

class OrderInput(graphene.InputObjectType):
    customer_id = graphene.ID(required=True)
    product_ids = graphene.List(graphene.ID, required=True)
    order_date = graphene.String()  # optional ISO datetime string

# --- Mutations ---

class CreateCustomer(graphene.Mutation):
    class Arguments:
        input = CustomerInput(required=True)

    customer = graphene.Field(CustomerType)
    message = graphene.String()
    errors = graphene.List(graphene.String)

    @classmethod
    def mutate(cls, root, info, input):
        errors = []
        if Customer.objects.filter(email=input.email).exists():
            errors.append("Email already exists")
        if input.phone and not is_valid_phone(input.phone):
            errors.append("Invalid phone format. Use +1234567890 or 123-456-7890")
        if errors:
            return CreateCustomer(customer=None, message="Validation failed", errors=errors)

        customer = Customer.objects.create(
            name=input.name,
            email=input.email,
            phone=input.phone or ""
        )
        return CreateCustomer(customer=customer, message="Customer created successfully.", errors=None)

class BulkCreateCustomers(graphene.Mutation):
    class Arguments:
        input = graphene.List(CustomerInput, required=True)

    customers = graphene.List(CustomerType)
    errors = graphene.List(graphene.String)

    @classmethod
    def mutate(cls, root, info, input):
        created = []
        errors = []

        with transaction.atomic():
            for idx, data in enumerate(input):
                try:
                    if Customer.objects.filter(email=data.email).exists():
                        raise Exception(f"Row {idx + 1}: Email '{data.email}' already exists")
                    if data.phone and not is_valid_phone(data.phone):
                        raise Exception(f"Row {idx + 1}: Invalid phone format")
                    customer = Customer.objects.create(
                        name=data.name,
                        email=data.email,
                        phone=data.phone or ""
                    )
                    created.append(customer)
                except Exception as e:
                    errors.append(str(e))

        return BulkCreateCustomers(customers=created, errors=errors or None)

class CreateProduct(graphene.Mutation):
    class Arguments:
        input = ProductInput(required=True)

    product = graphene.Field(ProductType)
    message = graphene.String()
    errors = graphene.List(graphene.String)

    @classmethod
    def mutate(cls, root, info, input):
        errors = []
        if input.price <= 0:
            errors.append("Price must be positive")
        if input.stock is not None and input.stock < 0:
            errors.append("Stock cannot be negative")
        if errors:
            return CreateProduct(product=None, message="Validation failed", errors=errors)

        product = Product.objects.create(
            name=input.name,
            price=input.price,
            stock=input.stock or 0
        )
        return CreateProduct(product=product, message="Product created successfully", errors=None)

class CreateOrder(graphene.Mutation):
    class Arguments:
        input = OrderInput(required=True)

    order = graphene.Field(OrderType)
    message = graphene.String()
    errors = graphene.List(graphene.String)

    @classmethod
    def mutate(cls, root, info, input):
        errors = []

        try:
            customer = Customer.objects.get(pk=input.customer_id)
        except Customer.DoesNotExist:
            errors.append("Invalid customer ID")

        products = Product.objects.filter(pk__in=input.product_ids)
        if not products.exists():
            errors.append("At least one valid product ID is required")

        if errors:
            return CreateOrder(order=None, message="Validation failed", errors=errors)

        total_amount = sum(p.price for p in products)
        order_date = now()
        if input.order_date:
            parsed_date = parse_datetime(input.order_date)
            if parsed_date:
                order_date = parsed_date

        order = Order.objects.create(
            customer=customer,
            total_amount=total_amount,
            order_date=order_date
        )
        order.products.set(products)
        return CreateOrder(order=order, message="Order created successfully", errors=None)
