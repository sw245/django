from django.shortcuts import render,redirect
from .models import Board
from django.db.models import F
import builtins

# Create your views here.
def list(request):
    qs = Board.objects.order_by('-bgroup','bstep')
    
    return render(request,'list.html',{'list':qs})

def write(request):
    if request.method == 'GET':
        return render(request,'write.html')
    
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        qs = Board.objects.create(title=title,content=content)
        qs.bgroup = qs.no
        qs.save()
        return redirect('/board/list/')
    

def view(request,no):
    qs = Board.objects.get(no=no)
    return render(request,'view.html',{'post':qs})
        
def reply(request,no):
    qs = Board.objects.get(no=no)
    if request.method == 'GET':
        return render(request,'reply.html',{'post':qs})
    
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        bgroup = request.POST.get('bgroup')
        # bstep = int(request.POST.get('bstep'))
        bindent = int(request.POST.get('bindent'))
        reply_bsteps = Board.objects.filter(bgroup=bgroup).values_list('bstep',flat=True)
        print(reply_bsteps)
        list_bsteps = builtins.list(reply_bsteps)
        bstep = max(list_bsteps) + 1
        Board(title=title,content=content,bgroup=bgroup,bstep=bstep,bindent=bindent+1).save()
        
        return redirect('/board/list/')
        

def update(request,no):
    qs = Board.objects.get(no=no)
    if request.method == 'GET':
        return render(request,'update.html',{'post':qs})
    
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        qs.title = title
        qs.content = content
        qs.save()
        return redirect(f'/board/view/{no}/')
        
        
def delete(request,no):
    qs = Board.objects.get(no=no)
    qs.delete()
    return redirect('/board/list/')