from django.shortcuts import render,redirect
from .models import Student

# Create your views here.
def list(request):
    qs = Student.objects.all()
    context = {'list':qs}
    return render(request,'students/list.html',context)



# 학생등록 페이지
def write(request):
    return render(request,'students/write.html')
        
    
# 학생등록 저장
def write_ok(request):
    name = request.POST.get('name')
    major = request.POST['major']       ## 이렇게 해도 됨
    grade = request.POST.get('grade')
    age = request.POST['age']
    gender = request.POST['gender']
    hobbys = request.POST.getlist('hobby')
    hobby = ','.join(hobbys)
    Student(name=name,major=major,grade=grade,age=age,gender=gender,memo='웹에서 등록됨',hobby=hobby).save()
    return redirect('/students/list/')


def view(request,no):
    try:
        qs = Student.objects.get(no=no)
    except:
        qs = None
    context = {'stu':qs}
    return render(request,'students/view.html',context)


def update(request,no):
    qs = Student.objects.get(no=no)     # set타입으로 받음
    context = {'stu':qs}
    # qs = Student.objects.filter(no=no)     # list타입으로 받음, 못 찾아도 에러 x
    # context = {'stu':qs[0]}
    return render(request,'students/update.html',context)

def update_ok(request):
    no = request.POST.get('no')
    hobbys = request.POST.getlist('hobby')
    hobby = ','.join(hobbys)
    qs = Student.objects.get(no=no)
    qs.name = request.POST.get('name')
    qs.major = request.POST.get('major')
    qs.grade = request.POST.get('grade')
    qs.age = request.POST.get('age')
    qs.gender = request.POST.get('gender')
    qs.hobby = hobby
    qs.save()
    return redirect(f'/students/view/{no}/')

def delete(request,no):
    Student.objects.get(no=no).delete()
    # return redirect('/students/list/')
    return redirect('students:list')    # (app_name:path name)  url보다 name으로 하는 게 더 좋음