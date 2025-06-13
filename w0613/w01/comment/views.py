from django.shortcuts import render
from django.http import JsonResponse
from .models import Comment
from member.models import Member
from board.models import Board

# Create your views here.

# 댓글 - Json타입으로 리턴
def dummy(request):
    context = {'result':'success'}
    return JsonResponse(context)

def cwrite(request):
    id = request.POST.get('id')
    bno = request.POST.get('bno')
    cpw = request.POST.get('cpw','')
    ccontent = request.POST.get('ccontent')
    # print('넘어온 데이터 :',id,cpw,ccontent)
    # id >> member, bno >> board 로 바꿔서 db에 저장해야 함
    member = Member.objects.get(id=id)
    board = Board.objects.get(bno=bno)
    
    
    # db 저장
    qs = Comment.objects.create(member=member,board=board,cpw=cpw,ccontent=ccontent)
    # print(qs)   # QuerySet 타입
    
    # Json타입 변환 - QuerySet list타입 << filter() / all() 은 list타입으로 바로 변경 가능
    # qss = Comment.objects.filter(cno=qs.cno)
    qs_list = Comment.objects.filter(cno=qs.cno).values()
    # print(qss)
    # print(qs_list)
    json_qs = list(qs_list)
    # print(json_qs)
    
    context = {'result':'성공','comment':json_qs}
    return JsonResponse(context)


def cdelete(request):
    cno = request.POST.get('cno')
    # print('넘어온 cno',cno)
    # db삭제
    Comment.objects.get(cno=cno).delete()
    
    context = {'result':'성공'}
    return JsonResponse(context)


def cupdate(request):
    cno = request.POST.get('cno')
    ccontent = request.POST.get('ccontent')
    
    qs = Comment.objects.get(cno=cno)
    qs.ccontent = ccontent
    qs.save()
    
    # json타입으로 변경
    json_qs = list(Comment.objects.filter(cno=cno).values())
    context = {'result':'success','comment':json_qs}
    return JsonResponse(context)
    