from django.shortcuts import render
from .models import Event

# Create your views here.
def list(request):
    qs = Event.objects.all()
    context = {'list':qs}
    return render(request,'event/list.html',context)