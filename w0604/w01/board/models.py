from django.db import models

# Create your models here.
class Board(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(null=True)
    title = models.CharField()
    content = models.TextField()
    bdate = models.DateField(auto_now=True)
    
    
    bgroup = models.IntegerField(default=0)
    bindent = models.IntegerField(default=0)
    bstep = models.IntegerField(default=0)
    
    bfile = models.ImageField(null=True,blank=True,upload_to='board')
    # bfile2 = models.FileField(null=True,blank=True,upload_to='board')
    # 모든파일 업로드 가능
    bhit = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.title
    
    
    