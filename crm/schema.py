<<<<<<< HEAD
from django.core.exceptions import ValidationError as DjangoValidationError
import graphene
from .types import CustomerType, ProductType, OrderType
from .models import Customer, Product, Order

# Input types for mutations
class CustomerInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    email = graphene.String(required=True)
    phone = graphene.String(required=False)

class ProductInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    price = graphene.Decimal(required=True)
    stock = graphene.Int(required=False, default_value=0)

class OrderInput(graphene.InputObjectType):
    customerId = graphene.ID(required=True)
    productIds = graphene.List(graphene.ID, required=True)
    orderDate = graphene.DateTime(required=False)

# Mutations

class CreateCustomer(graphene.Mutation):
    class Arguments:
        input = CustomerInput(required=True)

    customer = graphene.Field(CustomerType)
    message = graphene.String()
    errors = graphene.List(graphene.String)

    @classmethod
    def mutate(cls, root, info, input):
        try:
            temp_customer = Customer(name=input.name, email=input.email, phone=input.phone)
            temp_customer.full_clean()
            customer = Customer.objects.create(
                name=input.name,
                email=input.email,
                phone=input.phone
            )
            return CreateCustomer(customer=customer, message="Customer created successfully", errors=None)
        except DjangoValidationError as e:
            error_messages = [f"{field}: {', '.join(msgs)}" for field, msgs in e.message_dict.items()]
            return CreateCustomer(customer=None, message="Validation failed", errors=error_messages)
        except Exception as e:
            return CreateCustomer(customer=None, message="Unexpected error", errors=[str(e)])

class CreateProduct(graphene.Mutation):
    class Arguments:
        input = ProductInput(required=True)

    product = graphene.Field(ProductType)
    message = graphene.String()
    errors = graphene.List(graphene.String)

    @classmethod
    def mutate(cls, root, info, input):
        try:
            temp_product = Product(name=input.name, price=input.price, stock=input.stock)
            temp_product.full_clean()
            product = Product.objects.create(
                name=input.name,
                price=input.price,
                stock=input.stock
            )
            return CreateProduct(product=product, message="Product created successfully", errors=None)
        except DjangoValidationError as e:
            error_messages = [f"{field}: {', '.join(msgs)}" for field, msgs in e.message_dict.items()]
            return CreateProduct(product=None, message="Validation failed", errors=error_messages)
        except Exception as e:
            return CreateProduct(product=None, message="Unexpected error", errors=[str(e)])

class CreateOrder(graphene.Mutation):
    class Arguments:
        input = OrderInput(required=True)

    order = graphene.Field(OrderType)
    message = graphene.String()
    errors = graphene.List(graphene.String)

    @classmethod
    def mutate(cls, root, info, input):
        try:
            customer = Customer.objects.get(pk=input.customerId)
            products = Product.objects.filter(pk__in=input.productIds)

            if products.count() != len(input.productIds):
                missing_ids = set(input.productIds) - set(str(p.pk) for p in products)
                return CreateOrder(order=None, message="Some products not found", errors=[f"Missing product IDs: {', '.join(missing_ids)}"])

            order = Order.objects.create(customer=customer, order_date=input.orderDate or None)
            order.products.set(products)
            order.save()
            return CreateOrder(order=order, message="Order created successfully", errors=None)
        except Customer.DoesNotExist:
            return CreateOrder(order=None, message="Customer not found", errors=["Invalid customer ID"])
        except DjangoValidationError as e:
            error_messages = [f"{field}: {', '.join(msgs)}" for field, msgs in e.message_dict.items()]
            return CreateOrder(order=None, message="Validation failed", errors=error_messages)
        except Exception as e:
            return CreateOrder(order=None, message="Unexpected error", errors=[str(e)])

# Query class

class Query(graphene.ObjectType):
=======
import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .types import CustomerType, ProductType, OrderType
from .mutations import CreateCustomer, BulkCreateCustomers, CreateProduct, CreateOrder

class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hello, GraphQL!")
    
    # Basic queries returning all records
>>>>>>> 275468b69b688680d4983880ca426f02ac258e14
    customers = graphene.List(CustomerType)
    products = graphene.List(ProductType)
    orders = graphene.List(OrderType)

    def resolve_customers(root, info):
<<<<<<< HEAD
        return Customer.objects.all()

    def resolve_products(root, info):
        return Product.objects.all()

    def resolve_orders(root, info):
        return Order.objects.all()

# Mutation class

class Mutation(graphene.ObjectType):
    create_customer = CreateCustomer.Field()
=======
        return CustomerType._meta.model.objects.all()

    def resolve_products(root, info):
        return ProductType._meta.model.objects.all()

    def resolve_orders(root, info):
        return OrderType._meta.model.objects.all()

class Mutation(graphene.ObjectType):
    create_customer = CreateCustomer.Field()
    bulk_create_customers = BulkCreateCustomers.Field()
>>>>>>> 275468b69b688680d4983880ca426f02ac258e14
    create_product = CreateProduct.Field()
    create_order = CreateOrder.Field()
