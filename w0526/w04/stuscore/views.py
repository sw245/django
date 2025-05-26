from django.shortcuts import render
from .models import Stuscore

# Create your views here.
def list_s(request):
    qs = Stuscore.objects.all()
    context = {'list':qs}
    return render(request, 'list_s.html',context)