from django.shortcuts import render
from django.http import JsonResponse
from .models import Comment

# Create your views here.
def cwrite(request):
    cpw = request.POST.get('cpw')
    ccontent = request.POST.get('ccontent')
    
    qs = Comment(cpw=cpw,ccontent=ccontent)
    qs.save()
    
    qs_list = Comment.objects.filter(cno=qs.cno).values()
    qs_json = list(qs_list)
    

    context = {'comment',qs_json}
    return JsonResponse(context)