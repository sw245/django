from django.shortcuts import render
from django.http import JsonResponse
from .models import Comment

# Create your views here.
def list(request):
    context = {}
    return render(request,'customer/list.html',context)


def cdelete(request):
    cno = request.POST.get('cno')
    Comment.objects.get(cno=cno).delete()
    
    context = {'result':'sosad'}
    return JsonResponse(context)