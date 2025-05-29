from django.db import models

# Create your models here.
class Student(models.Model):
    no = models.AutoField(primary_key=True) # 번호가 순차적으로 증가
    name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    grade = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10,blank=True)
    hobby = models.CharField(max_length=100,blank=True)
    sdate = models.DateTimeField(auto_now=True) # 오라클의 date객체 - sysdate
    memo = models.TextField(blank=True)
    
    def __str__(self):
        return f'{self.no}, {self.name}, {self.sdate}'