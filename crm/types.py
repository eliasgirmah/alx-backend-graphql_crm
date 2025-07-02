import graphene
from graphene_django import DjangoObjectType
from .models import Customer, Product, Order

class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer
<<<<<<< HEAD
        fields = ("id", "name", "email", "phone")
=======
        fields = ('id', 'name', 'email', 'phone')
>>>>>>> 275468b69b688680d4983880ca426f02ac258e14

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
<<<<<<< HEAD
        fields = ("id", "name", "price", "stock")
=======
        fields = ('id', 'name', 'price', 'stock')
>>>>>>> 275468b69b688680d4983880ca426f02ac258e14

class OrderType(DjangoObjectType):
    class Meta:
        model = Order
<<<<<<< HEAD
        fields = ("id", "customer", "products", "order_date")

    # If you want to customize the products field to return a list of ProductType
    products = graphene.List(ProductType)

    def resolve_products(self, info):
        return self.products.all()
=======
        fields = ('id', 'customer', 'products', 'order_date', 'total_amount')
>>>>>>> 275468b69b688680d4983880ca426f02ac258e14
