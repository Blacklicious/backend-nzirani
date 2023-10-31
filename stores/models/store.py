from django.db import models
from .employee import Employee

# Store Data
class Store(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    operating_hours = models.CharField(max_length=100)  # e.g. "9:00 AM - 8:00 PM"
    employees = models.ManyToManyField(Employee, related_name='workplace')
    capacity = models.IntegerField(help_text="Maximum number of customers allowed at one time")
    registration_date = models.DateField()

    # If there are multiple branches or outlets, we can have a parent-child relationship
    parent_store = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='branches')

    def __str__(self):
        return self.name
