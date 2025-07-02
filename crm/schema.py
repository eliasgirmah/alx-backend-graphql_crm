import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .types import CustomerType, ProductType, OrderType
from .filters import CustomerFilter, ProductFilter, OrderFilter
from .mutations import CreateCustomer, BulkCreateCustomers, CreateProduct, CreateOrder

class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hello, GraphQL!")
    all_customers = DjangoFilterConnectionField(CustomerType, filterset_class=CustomerFilter)
    all_products = DjangoFilterConnectionField(ProductType, filterset_class=ProductFilter)
    all_orders = DjangoFilterConnectionField(OrderType, filterset_class=OrderFilter)

class Mutation(graphene.ObjectType):
    create_customer = CreateCustomer.Field()
    bulk_create_customers = BulkCreateCustomers.Field()
    create_product = CreateProduct.Field()
    create_order = CreateOrder.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
