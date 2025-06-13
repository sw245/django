from django.shortcuts import render
from .models import Board
from comment.models import Comment
from member.models import Member

# Create your views here.
# 게시판 리스트
def list(request):
    qs = Board.objects.all().order_by('-ntchk','-bgroup','bstep')
    context = {'list':qs}
    return render(request,'board/list.html',context)

# 게시글 보기
def view(request,bno):
    qs = Board.objects.get(bno=bno)
    c_qs = Comment.objects.filter(board=qs).order_by('-cno')
    context = {'view':qs,'clist':c_qs}   # filter로 받았을 시 qs 인덱싱 필요
    return render(request,'board/view.html',context)

