
from django.db import models
from .client import Client
from .item import Item
from .logistic import Logistics


# Sales Data
class Sale(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    quantity = models.IntegerField()
    logistics = models.ForeignKey(Logistics, on_delete=models.SET_NULL, null=True, blank=True, related_name='sales')
