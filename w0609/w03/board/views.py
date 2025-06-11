from django.shortcuts import render

# ajax 전송에 필요한 선언
from django.http import JsonResponse

# from django.core import serializers # list타입으로 변환? > json타입
# from django.views.decorators.csrf import csrf_exempt #csrf토큰이 없을때 예외처리

# Create your views here.
def list(request):
    return render(request,'board/list.html')
    
        

# form 전송방법
def view(request):
    if request.method == 'GET':
        return render(request,'board/view.html')
    elif request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        context = {'id':id,'name':name}
        return render(request,'board/view.html',context)
    
    
# ajax 전송방법
def view2(request):
    if request.method == 'GET':
        return render(request,'board/view.html')
    elif request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        # QuerySet, QueryList >> list타입으로 변경
        # models db데이터가 있으면, list타입으로 변경 후 전송해야 함.
        
        context = {'id':id,'name':name,'result':'success','pw':'1111'}
        
        return JsonResponse(context)