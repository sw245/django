from django.db import models
from board.models import Board
from board.models import Member

# Create your models here.
class Comment(models.Model):
    cno = models.AutoField(primary_key=True)
    board = models.ForeignKey(Board,on_delete=models.CASCADE)   # 게시글 삭제 시 댓글도 삭제
    member = models.ForeignKey(Member,on_delete=models.DO_NOTHING)  # 작성자 탈퇴 시
    cpw = models.CharField(max_length=20,null=True,blank=True)
    ccontent = models.TextField(blank=True)
    cdate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.cno}, {self.member.id}, {self.ccontent}'