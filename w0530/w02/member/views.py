from django.shortcuts import render,redirect
from .models import Member

# Create your views here.
def login(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        
        try:
            mem = Member.objects.get(id=id,pw=pw)
            request.session['session_id']  = id
            txt = 1
        except:
            txt = 0
        
        context = {'msg':txt}
        return render(request,'member/login.html',context)
        
    elif request.method == 'GET':
        return render(request,'member/login.html')
    
    
def logout(request):
    request.session.clear() # 모두 삭제
    return redirect('/')