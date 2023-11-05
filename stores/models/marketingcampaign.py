from django.db import models

# Marketing Data
class MarketingCampaign(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    impact_on_sales = models.TextField()

    def __str__(self):
        return self.name
