import graphene
from graphene_django.types import DjangoObjectType
from graphene import relay
from .models import Customer, Product, Order

class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer
        interfaces = (relay.Node,)  # ✅ Relay interface for filtering support
        filter_fields = ['name', 'email', 'phone', 'created_at']

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        interfaces = (relay.Node,)
        filter_fields = ['name', 'price', 'stock']

class OrderType(DjangoObjectType):
    class Meta:
        model = Order
        interfaces = (relay.Node,)
        filter_fields = ['order_date', 'total_amount', 'customer__name', 'products__name']
