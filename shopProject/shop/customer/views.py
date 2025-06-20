from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from customer.models import Customer
from member.models import Member
import datetime
from django.db.models import F
from comment.models import Comment

# Create your views here.
# get: 리스트페이지 / post: ??
def list(request):
    qs = Customer.objects.all().order_by('-bgroup','bstep')
    
    # 요청하는 페이지 번호 가져오기 str >> int타입 형 변환 필요
    page = int(request.GET.get('page',1))
    # 10개 단위 묶음
    paginator = Paginator(qs,10)
    # 가져올 페이지 선택
    customerList = paginator.get_page(page)
    # print('-----------------------------')
    # print(customerList)
    # print('-----------------------------')
    
    context = {'list':customerList,'page':page}
    return render(request,'customer/list.html',context)


def view(request,bno):
    qs = Customer.objects.get(bno=bno)
    
    # comment DB연결
    c_qs = Comment.objects.filter(board=qs)
    
    
    qs.bhit += 1
    qs.save()
    context = {'view':qs,'clist':c_qs}
    response = render(request,'customer/view.html',context)
    
    # # 쿠키이름 지정 - cookie_bhit: aaa, cookie_bhit: bbb, cookie_bhit: ccc
    # cookie_name = f'cookie_bhit:{request.session["session_id"]}'
    
    # # 쿠키시간 설정 - 1일기준
    # # tomorrow = datetime.datetime.now()  # 현재시간
    
    # # 해당일의 마지막 시간으로 설정
    # tomorrow = datetime.datetime.replace(datetime.datetime.now(),
    #                                      hour=23,minute=59,second=59)
    
    # # 쿠키시간으로 설정형태 변경
    # expires = datetime.datetime.strftime(tomorrow,'%a,%d-%b-%Y %H:%M:%S GMT')
    
    
    
    # if request.COOKIES.get(cookie_name) is not None:
    #     cookies = request.COOKIES.get(cookie_name)
    #     print('쿠키 :',cookies)
        
    # else:
    #     response.set_cookie(cookie_name,bno,expires=expires)
    #     qs.update(bhit = F('bhit')+1)

    # # 쿠키 확인
    # if request.COOKIES.get('cookie_name') is not None :
    #     ## 조회수방지 쿠키가 있을 때
    #     cookies = request.COOKIES.get('cookie_name')
    # else:
    #     ## 조회수방지 쿠키가 없을 때
    #     response.set_cookie('cookie_name',bno,expires=)
    # request.COOKIES.get('cookie_bhit')
    
    return response
    


def write(request):
    if request.method == 'GET':
        return render(request,'customer/write.html')
    elif request.method == 'POST':
        ## session은 서버에 있음
        id = request.session['session_id']
        # member = Member.objects.get(id=id)
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.FILES.get('bfile','')
        bfile2 = request.FILES.get('bfile2','')
        qs = Customer.objects.create(btitle=btitle,id=id,bcontent=bcontent,bfile=bfile,bfile2=bfile2)
        qs.bgroup = qs.bno
        qs.save()
        print('-----------------')
        print(btitle)
        print('-----------------')
        context = {'msg':1}
        return render(request,'customer/write.html',context)
        # return redirect('/customer/list/')
        
        
def delete(request,bno):
    pass


def update(request,bno):
    if request.method == 'GET':
        return render(request,'customer/update.html')
    elif request.method == 'POST':
        btitle = request.GET.get('btitle')
        id = request.GET.get('id')
        bcontent = request.GET.get('bcontent')
        bfile = request.GET.get('bfile')
        bfile2 = request.GET.get('bfile2')
        
        
        response = redirect('/customer/view//')
        return response

