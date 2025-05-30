from django.shortcuts import render,redirect
from .models import Member

# Create your views here.

# 로그인 페이지: get방식 접속 / 로그인 확인: post방식 접속
def login(request):
    if request.method == 'GET':
        return render(request,'member/login.html')
    
    elif request.method == 'POST': 
        # 입력된 정보 
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        context = {}
        try:
            qs = Member.objects.get(id=id)
            if qs.pw == pw:
                request.session['session_id'] = id      # session 할당
                txt = 1     # 성공
            else:
                txt = -1
                # print('비밀번호가 일치하지 않습니다.')
        except:
            # print('아이디가 존재하지 않습니다.')
            txt = 0     # 실패
        
        
        
        # DB에서 조회
        # try:
        #     qs = Member.objects.get(id=id,pw=pw)
        #     request.session['session_id'] = id      # session 할당
        #     # request.session.clear() # session 모두 삭제
        #     # del request.session['session_id']   # session 1개 삭제
        #     # print(qs)
        #     txt = 1     # 성공
        # except:
        #     # print('아이디 또는 패스워드가 일치하지 않습니다.')
        #     txt = 0     # 실패
        
        context = {'msg':txt}
        return render(request,'member/login.html',context)
        
        # return redirect('/')
    

def logout(request):
    request.session.clear() # 세션 삭제 // 1개만 삭제: del request.session['session_id']
    context = {'msg':2}
    return render(request,'member/login.html',context)