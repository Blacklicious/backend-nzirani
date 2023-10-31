from django.db import models
from .item import Item
from .logistic import Logistics
from .client import Client


# Purchase Data (link between Client and Item)
class Purchase(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date = models.DateField()
    feedback = models.TextField(blank=True, null=True)
    logistics = models.ForeignKey(Logistics, on_delete=models.SET_NULL, null=True, blank=True, related_name='purchases')
