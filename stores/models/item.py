from django.db import models

# Base Item Model for both Product and Service
class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        abstract = True

# Product Model
class Product(Item):
    stock_quantity = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Purchase cost
    supplier = models.ForeignKey('Supplier', on_delete=models.SET_NULL, null=True, related_name='supplied_products')

# Service Model
class Service(Item):
    duration = models.DurationField()  # Duration of the service
    provider = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, related_name='provided_services')

