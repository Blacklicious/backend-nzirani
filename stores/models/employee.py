from django.db import models

# Employee Data
class Employee(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact = models.CharField(max_length=20)
    hire_date = models.DateField()
    job_role = models.CharField(max_length=100)
    performance_review = models.TextField(blank=True, null=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
