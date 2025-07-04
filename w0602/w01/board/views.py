from django.shortcuts import render,redirect
from .models import Board
from django.core.paginator import Paginator


# Create your views here.
def list(request):
    # 모든 데이터 가져오기
    qs = Board.objects.all().order_by('-bno')
    # 페이지 설정
    paginator = Paginator(qs,5)    # 총 게시글을 페이지로 분할
    page = int(request.GET.get('page',1))   # 현재페이지 가져오기
    list_p = paginator.get_page(page)     # 해당 페이지 가져오기
    context = {'list':list_p,'page':page}
    return render(request,'board/list.html',context)

def write(request):
    if request.method == 'GET':
        return render(request,'board/write.html')
    elif request.method == 'POST':
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        qs = Board(btitle=btitle, bcontent=bcontent, id='aaa')
        # qs.bgroup = qs.bno
        qs.save()
        # print(btitle, bcontent, bfile,qs.bgroup,qs.bstep)
        
        
        return redirect('board:list')
    
    
def view(request,bno):
    qs = Board.objects.get(bno=bno)
    context = {'board':qs}
    return render(request,'board/view.html',context)


def update(request,bno):
    if request.method == 'GET':
        qs = Board.objects.get(bno=bno)
        context = {'board':qs}
        return render(request,'board/update.html',context)
        
    elif request.method == 'POST':
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        context = {'msg':1}
        return render(request,'board/update.html',context)
        
        