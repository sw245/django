from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list(request):
    # return HttpResponse('리스트 페이지.....')
    return render(request,'list.html')

def write(request):
    return render(request, 'write.html')

def delete(request):
    return render(request, 'delete.html')

def view(request):
    return render(request, 'view.html')