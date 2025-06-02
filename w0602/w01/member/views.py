from django.shortcuts import render,redirect
from .models import Member

## went wrong ##

# Create your views here.
def login(request):
    return render(request,'member/login.html')

def logout(request):
    request.session.clear()
    context = {'msg':-1}
    return render(request,'member/login.html',context)

def submit(request):
    # 쿠키를 읽어와서 idcheck라는 쿠키가 있으면, 저장된 아이디를 리턴
    # 모든 쿠키 읽어오기 request.COOKIES
    # 특정 쿠키 읽어오기 
    
    
    request.COOKIES.get('idcheck','') # 없으면 ''
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    idcheck = request.POST.get('idcheck')
    
    try:
        qs = Member.objects.get(id=id,pw=pw)
        context = {'msg':1}
    except:
        context = {'msg':0}
        return render(request,'member/login.html',context)
    
    # 세션 저장?
    request.session['session_id'] = id
    request.session['session_nickname'] = qs.nickname
    
    
    response = render(request,'member/login.html',context)
    
    if idcheck:
        # print('idcheck : checked')
        response.set_cookie('saved_id',id)
    else: 
        response.delete_cookie('saved_id')
    # try: Member.objects.get(id=id,pw=pw)
    # except: pass
        
    return response


def join01(request):
    return render(request,'member/join01.html')

def join02(request):
    if request.method == 'GET':
        return render(request,'member/join02.html')
    elif request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw1')
        name = request.POST.get('name')
        nickname = request.POST.get('nickname')
        f_tel = request.POST.get('f_tell')
        m_tel = request.POST.get('m_tell')
        l_tel = request.POST.get('l_tell')
        tel = f'{f_tel}-{m_tel}-{l_tel}'
        gender = request.POST.get('gender')
        hobbys = request.POST.getlist('hobby')
        hobby = ','.join(hobbys)
        Member(id=id,pw=pw,name=name,nickname=nickname,tel=tel,gender=gender,hobby=hobby).save()
        
        print('넘어온 데이터 :',id,pw,name,nickname,tel,gender,hobby)
        
        return redirect('/member/join03/')
    
def join03(request):
    return render(request,'member/join03.html')