from django.shortcuts import render
from .models import Student

# Create your views here.
def list(request):
    qs = Student.objects.all()
    context = {'list':qs}
    return render(request,'students/list.html',context)