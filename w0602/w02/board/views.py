from django.shortcuts import render,redirect
from .models import Board

# Create your views here.
def list(request):
    return render(request,'board/list.html')

def write(request):
    if request.method == 'GET':
        return render(request,'board/write.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        file = request.POST.get('file')
        Board(name='aaa',title=title,content=content).save()
    
        return redirect('board:list')