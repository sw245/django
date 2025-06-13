from django.db import models

# Create your models here.
class Comment(models.Model):
    cno = models.AutoField(primary_key=True)
    member = models.CharField(max_length=100,default='aaa')
    cpw = models.CharField(max_length=20,null=True,blank=True)
    ccontent = models.TextField(blank=True)
    cdate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.cno},{self.member.id},{self.ccontent}'
    