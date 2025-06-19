from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Member
import random
import numpy as np


## 
def login(request):
    # get: 로그인 페이지 / host: 로그인 확인
    if request.method == 'GET':
        return render(request,'member/login.html')
    
    elif request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        idsave = request.POST.get('idsave')
        print('id,pw,idsave :',id,pw,idsave)
        
        qs = Member.objects.filter(id=id,pw=pw)   # filter >> 없으면 None // get >> 없으면 error
        
        #세션 설정
        if not qs:
            msg = 0
            request.session['session_id'] = id
            request.session['session_name'] = qs[0].name
        else:
            msg = 1
        
        context = {'msg':msg}
        
        # 쿠키 설정
        response = render(request,'member/login.html',context)
        
        if idsave:
            response.set_cookie('cook_id',id,max_age=60*60*24)
        else:
            response.delete_cookie('cook_id')
            
        return response
    
    
    
    
def step01(request):
    return render(request,'member/step01.html')


def emailSend(request):
    email = request.POST.get('email')
    print('전송할 이메일 주소:',email)
    
    txt = 'qwertyuiopasdfghjklzxcvbnm0123456789'
    random_array = []
    
    
    return JsonResponse(context)

