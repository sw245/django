from django.db import models

# Create your models here.
class Member(models.Model):
    id = models.CharField(max_length=50,primary_key=True)
    pw = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    tel = models.CharField(max_length=20,default='010-0000-0000')
    gender = models.CharField(max_length=10)
    hobby = models.CharField(max_length=100)
    mdate = models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self):
        return f'{self.id}, {self.name}, {self.nickname}'
    
    
    
    
    
    
    
