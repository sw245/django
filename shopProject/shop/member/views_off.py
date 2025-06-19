from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Member
import random
import numpy as np


## 
random_txt = ''


# Create your views here.
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
    return render(request, 'member/step01.html')


def logout(request):
    request.session.clear()
    msg = 0
    context = {'msg':msg}
    return render(request,'member/login.html',context)



## 랜덤번호 생성

def random_number():
    # 알파벳 26개, 숫자 10개: 36개 0-35
    txt = 'abcdefghijklmnopqrstuvwxyz0123456789'
    random_array = []
    random_array = np.random.randint(0,35,10)
    print('random array :',random_array)
    global random_txt
    random_txt = ''
    for i in random_array:
        random_txt += txt[i]
    return random_txt


def emailSend(request):
    email = request.POST.get('email')
    
    random_txt = random_number()
    ## 이메일 발송 부분
    
    print('넘어온 email:', email)
    
    context = {'msg':'success','random_txt':random_txt}
    return JsonResponse(context)


def confirmChk(request):
    confirmTxt = request.POST.get('confirmTxt')
    print('전송번호 :',confirmTxt)
    
    if confirmTxt == random_txt:
        confirm_ok = 1
    else:
        confirm_ok = 0
    
    context = {'confirm_ok':confirm_ok}
    return JsonResponse(context)