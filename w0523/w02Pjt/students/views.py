from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list(request):  
    return HttpResponse('리스트 페이지가 열립니다.')
    
    ## HttpResponse >> 입력한 문자열을 http파일로 변경해서 출력

def view(reuqest):  
    return HttpResponse('뷰 페이지를 오픈합니다.')


def write(request):
    return render(request,'write.html')     

def delete(request):
    return render(request,'delete.html')