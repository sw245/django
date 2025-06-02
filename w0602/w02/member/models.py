from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField()
    id = models.CharField(primary_key=True)
    pw = models.CharField()
    
    def __str__(self):
        return self.name