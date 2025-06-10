from django.shortcuts import render,redirect
from .models import Board
from member.models import Member
from django.core.paginator import Paginator

## 게시판리스트
def list(request):
    page = int(request.GET.get('page',1))
    qs = Board.objects.all().order_by('-ntchk','-bgroup','bstep')
    paginator = Paginator(qs,10)
    list_p = paginator.get_page(page)
    context = {'list':list_p,'page':page}
    return render(request,'board/list.html',context)

# 글쓰기: get, post
def write(request):
    if request.method == 'GET':
        return render(request,'board/write.html')
    elif request.method == 'POST':
        id = request.POST.get('id')
        member = Member.objects.get(id=id)
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.FILES.get('bfile')
        ntchk = request.POST.get('ntchk',0)
        # print('데이터 :',id,btitle,bcontent,bfile,ntchk)
        
        qs = Board.objects.create(member=member,btitle=btitle,bcontent=bcontent,bfile=bfile,ntchk=ntchk)
        # 답글달기 시 필요
        qs.bgroup = qs.bno
        qs.save()
        return redirect('/board/list/')
        # return render(request,'board/write.html')
        
        
def view(request,bno):
    # pre_qs = Board.objects.filter(
    #     Q(ntchk__lte=qs[0].ntchk,)
    # )
    # pre = Q(ntchk__lte=qs[0], bgroup__gt=qs[0].bgroup,bstep
    return render(request,'board/view.html')