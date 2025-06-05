from django.shortcuts import render,redirect
from .models import Board
from django.db.models import F,Q
from django.core.paginator import Paginator
import builtins

# Q - or 쓸 때 사용?
# F - 특정 컬럼 뽑아내기



# Create your views here.
# 게시판 리스트 - 일반 게시판리스트 / 검색된 글 리스트
def list(request):
    qs = Board.objects.order_by('-bgroup','bstep')
    # 현재 페이지
    page = int(request.GET.get('page',1))   # 페이지 넘버가 없으면 1으로 처리
    
    # search
    search = request.GET.get('search','')
    category = request.GET.get('category','')
    # print('검색데이터 :',search,category)
    
    
    if search == '':    # 일반 리스트(검색x)
        # print('search가 없을 때')
        # 페이지 분기
        paginator = Paginator(qs,20)    # 100개의 게시글을 10개씩 쪼개서 전달
        list_p = paginator.get_page(page)   # 현재페이지의 게시글을 전달
        return render(request,'list.html',{'list':list_p,'page':page})

    else:   # 검색된 글 리스트
        # print('search가 있을 때')
        if category == 'all':
            qs = Board.objects.filter(Q(title__icontains=search) | Q(content__icontains=search))
        elif category == 'btitle':
            qs = Board.objects.filter(title__icontains=search)
        elif category == 'bcontent':
            qs = Board.objects.filter(content__icontains=search)
        paginator = Paginator(qs,20)    # 100개의 게시글을 10개씩 쪼개서 전달
        list_p = paginator.get_page(page)   # 현재페이지의 게시글을 전달
        return render(request,'list.html',{'list':list_p,'page':page,'category':category,'search':search})
    

def write(request):
    if request.method == 'GET':
        return render(request,'write.html')
    
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        bfile = request.FILES.get('file','')   # 없을 때는 ''
        print('파일부분 :',request.FILES)
        print('bfile 가져온 데이터 :',bfile)
        qs = Board.objects.create(title=title,content=content,bfile=bfile)
        qs.bgroup = qs.no
        qs.save()
        return redirect('/board/list/')
    

def view(request,no):
    category = request.GET.get('category')
    search = request.GET.get('search')
    qs = Board.objects.get(no=no)
    return render(request,'view.html',{'post':qs,'category':category,'search':search})
        
def reply(request,no):
    qs = Board.objects.get(no=no)
    if request.method == 'GET':
        return render(request,'reply.html',{'post':qs})
    
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        bfile = request.FILES.get('file','')
        bgroup = request.POST.get('bgroup')
        # bstep = int(request.POST.get('bstep'))
        bindent = int(request.POST.get('bindent'))
        reply_bsteps = Board.objects.filter(bgroup=bgroup).values_list('bstep',flat=True)
        # print(reply_bsteps)
        list_bsteps = builtins.list(reply_bsteps)
        bstep = max(list_bsteps) + 1
        Board(title=title,content=content,bgroup=bgroup,bstep=bstep,bindent=bindent+1,bfile=bfile).save()
        
        return redirect('/board/list/')
        

def update(request,no):
    qs = Board.objects.get(no=no)
    if request.method == 'GET':
        return render(request,'update.html',{'post':qs})
    
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        bfile_pre = request.POST.get('bfile_pre','')
        bfile = request.FILES.get('file','')
        if not bfile:
            bfile = bfile_pre
        qs.bfile = bfile
        qs.title = title
        qs.content = content
        qs.save()
        return redirect(f'/board/view/{no}/')
        
        
def delete(request,no):
    qs = Board.objects.get(no=no)
    qs.delete()
    return redirect('/board/list/')