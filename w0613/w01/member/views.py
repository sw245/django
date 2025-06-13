from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mlist(request):
    return HttpResponse('<h2>멤버</h2>')