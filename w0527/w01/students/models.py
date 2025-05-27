from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    grade = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.name}, {self.major}'
    
# 변경사항 있으면 다시 makemigrations, migrate 해야 함
# migrations 폴더에 변경되기 전 파일 생성



# class Stu_write(models.Model):
    