from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField()
    hobby = models.CharField()
    interest = models.CharField()
    strength = models.CharField()
    desire = models.CharField()
    
    def __str__(self):
        return self.name