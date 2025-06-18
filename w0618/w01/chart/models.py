from django.db import models

# Create your models here.
class Profit(models.Model):
    year = models.IntegerField()
    monthly = models.CharField(max_length=10)
    totalSales = models.IntegerField(default=0)
    profit = models.IntegerField(default=0)
    
    