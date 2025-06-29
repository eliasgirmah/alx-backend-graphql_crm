import re
import graphene
from .models import Customer
from .types import CustomerType
from django.core.exceptions import ValidationError
from django.db import IntegrityError

# Helper for phone validation
def is_valid_phone(phone):
    return re.match(r'^(\+\d{10,15}|\d{3}-\d{3}-\d{4})$', phone)

class CreateCustomer(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        phone = graphene.String()

    customer = graphene.Field(CustomerType)
    message = graphene.String()

    def mutate(self, info, name, email, phone=None):
        # Validate email uniqueness
        if Customer.objects.filter(email=email).exists():
            raise Exception("Email already exists")

        # Validate phone format if provided
        if phone and not is_valid_phone(phone):
            raise Exception("Invalid phone format. Use +1234567890 or 123-456-7890")

        try:
            customer = Customer.objects.create(name=name, email=email, phone=phone or "")
            return CreateCustomer(customer=customer, message="Customer created successfully.")
        except ValidationError as e:
            raise Exception(f"Validation error: {e}")
        except IntegrityError:
            raise Exception("Integrity error: Possibly a duplicate email")
