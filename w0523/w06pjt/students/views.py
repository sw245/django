from django.shortcuts import render
from students.models import Students

# Create your views here.
def list(request):
    qs = Students.objects.all()
    return render(request,'list.html',{'students':qs})

def view(request):
    qs = Students.objects.get(name='이순신')
    return render(request,'view.html',{'student':qs})