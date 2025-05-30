from django.db import models

# Create your models here.
class Member(models.Model):
    id = models.CharField(primary_key=True)
    pw = models.CharField()
    nickname = models.CharField()
    tel = models.CharField(default='010-0000-0000')
    hobby = models.CharField()
    mdate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.id