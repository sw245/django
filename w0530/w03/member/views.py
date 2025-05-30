from django.shortcuts import render
from .models import Member

# Create your views here.
def login(request):
    # 쿠키 읽어오기
    cookie_info = request.COOKIES
    # 쿠키가 있으면: cookie_val / None: ''
    # cookie_id = request.COOKIES.get('cookie_val','')
    cookie_id = request.COOKIES.get('cookie_val')
    print(cookie_id)
    
    if request.method == 'GET': # login 페이지 열기
        context = {'cookie_id':cookie_id,'cookie_info':cookie_info}
        return render(request,'member/login.html',context)
    
    elif request.method == 'POST':  # ID/PW 확인
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        cookie_val = request.POST.get('cookie_val')
        try:
            qs = Member.objects.get(id=id,pw=pw)
            request.session['session_id'] = qs.id
            request.session['session_nickname'] = qs.nickname
            msg = 1     # id,pw 일치
        except:
            msg = 0     # id/pw 불일치
        
            
        context = {'msg':msg, 'cookie_info':cookie_info,'cookie_id':cookie_id}
        response = render(request,'member/login.html',context)
        # response에 쿠키 저장
        
        if cookie_val is not None:
            response.set_cookie('cookie_val',id,max_age=60*60*24)   # max_age >> 쿠키 지속시간(초) = 초*분*시간
        else:
            response.delete_cookie('cookie_val')
            
        
        return response
    
def logout(request):
    request.session.clear()
    context = {'msg':-1}
    return render(request,'member/login.html',context)