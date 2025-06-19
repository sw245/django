from django.shortcuts import render

# Create your views here.
def list(request):
    return render(request,'kakaomap/list.html')


def list2(request):
    return render(request, 'kakaomap/list2.html')

def list3(request):
    return render(request, 'kakaomap/list3.html')