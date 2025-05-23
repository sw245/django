from django.db import models

# ORM: Object Relational Mapping
# class 객체 등록하면 자동으로 db 생성
class Student(models.Model):
    name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    grade = models.IntegerField(default=0)
    gender = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

## SQL 쿼리문
# create table student (
    # name varchar2(100),
    # major varchar2(100),
# )
