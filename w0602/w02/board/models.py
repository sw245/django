from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField()
    content = models.CharField()
    
    def __str__(self):
        return self.title