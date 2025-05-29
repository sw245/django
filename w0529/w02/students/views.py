from django.shortcuts import render,redirect
from .models import Student

# Create your views here.
def list(request):
    qs = Student.objects.all()
    context = {'list':qs}
    return render(request,'list.html',context)


def write(request):
    return render(request,'write.html')

def write_ok(request):
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    Student(name=name,major=major,grade=grade,age=age,gender=gender).save()
    return redirect('/students/list/')


def view(request,no):
    qs = Student.objects.get(no=no)
    return render(request,'view.html',{'stu':qs})