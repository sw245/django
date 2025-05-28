from django.shortcuts import render,redirect
from .models import Student

# Create your views here.
def list(request):
    qs = Student.objects.all()
    context = {'list':qs}
    return render(request,'list.html',context)


def write(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        Student(name=name,major=major,grade=grade,age=age,gender=gender).save()
        return redirect('/students/list/')
    else: return render(request,'write.html')
    
    
def view(request):
    name = request.GET.get('name')
    qs = Student.objects.get(name=name)
    context = {'stu':qs}
    return render(request,'view.html',context)


def update(request,name):
    if request.method == 'GET':
        qs = Student.objects.get(name=name)
        context = {'stu':qs}
        return render(request,'update.html',context)
    elif request.method == 'POST':
        name_new = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        qs = Student.objects.get(name=name)
        qs.name = name_new
        qs.major = major
        qs.grade = grade
        qs.age = age
        qs.gender = gender
        qs.save()
        return redirect(f'/students/view/?name={name_new}')
    
    
def delete(request,name):
    Student.objects.get(name=name).delete()
    return redirect('/students/list/')