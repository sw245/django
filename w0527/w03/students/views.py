from django.shortcuts import render

# Create your views here.
def list(request):
    # request > 'id=aaa', pw=111
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    gender = request.POST.get('gender')
    phone = request.POST.get('phone')
    hobbys = request.POST.getlist('hobby')   # >> 체크박스는 리스트로 받아야 함
    print("입력된 id값:",request.POST.get('id'))
    print("입력된 pw값:",request.POST.get('pw'))
    context = {'id':id,'pw':pw,'gender':gender,'phone':phone,'hobby':hobbys}
    
    return render(request,'list.html',context)


def view(request):
    # get방식 (form이 아니면 모두 다 get 방식?)
    name = request.GET.get('name')
    age = request.GET.get('age')
    print('이름 :',name)
    print('나이 :',age)
    context = {'name':name,'age':age}
    return render(request, 'view.html',context)


def write(request):
    return render(request,'write.html')


def send(request,name,age):
    print('payload :',name,age)
    context = {'name':name,'age':age}
    return render(request,'send.html',context)