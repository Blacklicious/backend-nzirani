from django.db import models


# Generalized Logistics Model
class Logistics(models.Model):
    TYPE_CHOICES = [
        ('Shipping', 'Shipping'),
        ('In-Store Pickup', 'In-Store Pickup'),
        ('Delivery', 'Delivery'),
    ]
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    status = models.CharField(max_length=100)  # e.g., "In Transit", "Delivered", "Pending"
    provider = models.CharField(max_length=255, null=True, blank=True)  # e.g., "FedEx", "USPS", or null for in-store
    tracking_number = models.CharField(max_length=255, null=True, blank=True)
    estimated_delivery = models.DateField(null=True, blank=True)
    actual_delivery = models.DateField(null=True, blank=True)
