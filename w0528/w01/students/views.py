from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import Student

# Create your views here.
def list(request):
    ## DB 검색 ##
    # .objects.all(): 모두 검색,
    # .objects.get(): 특정 항목 검색(한 개 객체로 받음), 
    # .objects.filter(): 특정 항목 검색2(QuerySet으로 받음)
    # .objects.order_by('컬럼명'): 정렬, '-컬럼명' : 역순정렬
    # qs = Student.objects.all()
    qs = Student.objects.order_by('-id') # 순차정렬
    context = {'list':qs}    
    return render(request,'list.html',context)


def write(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        print(request.method)
        print('입력된 정보 :',name,major,grade,age,gender)
        ## DB에 저장 ##
        # 데이터 저장 1. save()
        Student(name=name,major=major,grade=grade,age=age,gender=gender).save()
        # 데이터 저장 2. create()
        # Student.objects.create(name=name,major=major,grade=grade,age=age,gender=gender)
        return redirect('/students/list/')
    else:   # GET 방식으로 들어올 때
        print(request.method)
        return render(request,'./write.html')
    

def view(request):
    name = request.GET.get('name')
    qs = Student.objects.get(name=name)
    context = {'stu':qs}
    # print(qs)
    return render(request,'view.html',context)


def update(request,name):
    if request.method == 'GET':
        print('학생이름 :',name)
        qs = Student.objects.get(name=name)
        context = {'name':name,'stu':qs}
        return render(request,'update.html',context)
    elif request.method == 'POST':
        # 데이터 받기
        name_new = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        # 정보 수정
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