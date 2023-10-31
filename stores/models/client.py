# Client Data ------ nzirani/models/client.py

from django.db import models
from .item import Item
from .purchase import Purchase 

class Client(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    address_gps = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    purchase_history = models.ManyToManyField(Item, through='Purchase')
    feedback = models.TextField(blank=True, null=True)

class Review(models.Model):
    client = models.ForeignKey(Client, related_name='reviews', on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField()  # You can add validation to limit this to, say, 1-5
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.client.name} - {self.rating} stars"