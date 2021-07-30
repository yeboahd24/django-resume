from localflavor.us.forms import USStateField
from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=25)
    email = models.EmailField()

    def __str__(self):
        return self.full_name

class Address(models.Model):
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=5)

    person = models.OneToOneField(Person, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.street
