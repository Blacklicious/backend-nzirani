from django.db import models


# Supplier Data
class Supplier(models.Model):
    company_name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
