from django.shortcuts import render,redirect
from .models import Board
from django.core.paginator import Paginator

# Create your views here.
def list(request):
    qs = Board.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(qs,3)
    list_paged = paginator.get_page(page)
    return render(request,'board/list.html',{'list':list_paged,'page':page})


def view(request,no):
    qs = Board.objects.get(no=no)
    return render(request,'board/view.html',{'view':qs})


def write(request):
    if request.method == 'GET':
        return render(request,'board/write.html')
    
    elif request.method == 'POST':
        title = request.POST.get('title')
        name = request.POST.get('name')
        content = request.POST.get('content')
        bfile = request.FILES.get('file')
        Board.objects.create(title=title,name=name,content=content,bfile=bfile)
        
        return redirect('/board/list/')
        