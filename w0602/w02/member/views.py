from django.shortcuts import render,redirect
from .models import Member

# Create your views here.
def login(request):
    if request.method == 'GET':
        context = {'msg':None} 
        return render(request,'member/login.html',context)
    elif request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        
        try:
            qs = Member.objects.get(id=id,pw=pw)
            msg = 1
        except:
            msg = 0
            
        context = {'msg':msg}
        return render(request,'member/login.html',context)
        