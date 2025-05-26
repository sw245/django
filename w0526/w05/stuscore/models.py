from django.db import models

# Create your models here.
class Stuscore(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    kor = models.IntegerField()
    eng = models.IntegerField()
    math = models.IntegerField()
    total = models.IntegerField()
    avg = models.IntegerField()
    
    def __str__(self):
        return f'{self.no}, {self.name}, {self.total}'