from django.db import models

# Create your models here.
class Student(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    grade = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    sdate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    