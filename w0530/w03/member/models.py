from django.db import models

# Create your models here.
class Member(models.Model):
    id = models.CharField(primary_key=True)
    pw = models.CharField()
    name = models.CharField()
    nickname = models.CharField()
    tel = models.CharField(default='010-0000-0000')
    gender = models.CharField()
    hobby = models.CharField()
    mdate = models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self):
        return f'{self.name}, {self.id}, {self.nickname}'