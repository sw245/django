from django.shortcuts import render,redirect
from .models import Board

# ajax 전송에 필요한 선언
from django.http import JsonResponse
from django.core import serializers

# from django.core import serializers # list타입으로 변환? > json타입
# from django.views.decorators.csrf import csrf_exempt #csrf토큰이 없을때 예외처리

# Create your views here.
def list(request):
    if request.method == 'GET':
        qs = Board.objects.all().order_by('-ntchk','-bgroup','bstep')
        context = {'list':qs}
        return render(request,'board/list.html',context)
    elif request.method == 'POST':
        id = request.POST.get('id')
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        # print('넘어온 데이터 :',id,btitle,bcontent)
        qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent)
        qs.bgroup = qs.bno
        qs.save()
        return redirect('/board/list/')
        

def view(request):
    bno = request.GET.get('bno')
    print('bno :',bno)
    qs = Board.objects.get(bno=bno)
    context = {'view':qs}
    return render(request,'board/view.html',context)


def list2(request):
    if request.method == 'GET':
        qs = Board.objects.all().order_by('-ntchk','-bgroup','bstep')
        context = {'list':qs}
        return render(request,'board/list2.html',context)
    elif request.method == 'POST':
        id = request.POST.get('id')
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        # print('넘어온 데이터 :',id,btitle,bcontent)
        qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent)
        qs.bgroup = qs.bno
        qs.save()
        return redirect('/board/list/')
        

def view2(request,bno):
    qs = Board.objects.get(bno=bno)
    context = {'view':qs}
    return render(request,'board/view.html',context)


def list3(request):
    qs = Board.objects.all().order_by('-ntchk','-bgroup','bstep')
    context = {'list':qs}
    return render(request,'board/list3.html',context)

def ajax3(request):
    qs = Board.objects.all().order_by('-ntchk','-bgroup','bstep')
    a = request.POST.get('sampleid')
    print('넘어온 데이터 :',a)
    list_qs = serializers.serialize('json',qs)
    print('list_qs :',list_qs)
    context = {'result':'success','list':list_qs}
    print(qs)
    return JsonResponse(context)

