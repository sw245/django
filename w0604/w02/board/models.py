from django.db import models

# Create your models here.
class Board(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    bgroup = models.IntegerField(default=0)
    bstep = models.IntegerField(default=0)
    bindent = models.IntegerField(default=0)
    
    bdate = models.DateField(auto_now=True)
    bhit = models.IntegerField(default=0)
    bfile = models.FileField(null=True,blank=True,upload_to='board')
    
    
    def __str__(self):
        return self.title