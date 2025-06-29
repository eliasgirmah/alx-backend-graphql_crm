import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .types import CustomerType, ProductType, OrderType
from .mutations import CreateCustomer, BulkCreateCustomers, CreateProduct, CreateOrder

class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hello, GraphQL!")
    
    # Basic queries returning all records
    customers = graphene.List(CustomerType)
    products = graphene.List(ProductType)
    orders = graphene.List(OrderType)

    def resolve_customers(root, info):
        return CustomerType._meta.model.objects.all()

    def resolve_products(root, info):
        return ProductType._meta.model.objects.all()

    def resolve_orders(root, info):
        return OrderType._meta.model.objects.all()

class Mutation(graphene.ObjectType):
    create_customer = CreateCustomer.Field()
    bulk_create_customers = BulkCreateCustomers.Field()
    create_product = CreateProduct.Field()
    create_order = CreateOrder.Field()
