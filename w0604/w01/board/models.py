from django.db import models

# Create your models here.
class Board(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(null=True)
    title = models.CharField()
    content = models.TextField()
    bdate = models.DateField(auto_now=True)
    
    bgroup = models.IntegerField(default=0)
    bstep = models.IntegerField(default=0)
    bindent = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    
    