from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('확인')
    
    
    return render(request,'index.html')

def test(request):
    name = request.POST.get('name')
    kor = request.POST.get('kor')
    eng = request.POST.get('eng')
    total = int(kor) + int(eng)
    hobbys = request.POST.getlist('hobby')
    context = {'name':name,'kor':kor,'eng':eng,'total':total,'hobbys':hobbys}
    return render(request,'test.html',context)