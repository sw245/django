from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Student
from django.urls import reverse

# Create your views here.
def list(request):
    # txt = '''
    #     <html>
    #         <head>
    #         </head>
    #         <body>
    #             <h2>학생 리스트</h2>
    #         </body>
    #     </html>
    # '''
    # return HttpResponse(txt)
    qs = Student.objects.all()
    context = {'list':qs}
    return render(request,'students/list.html',context)

def write(request):
    return render(request,'students/write.html')

def write2(request):
    # print(request.POST)
    # request.POST[] >> 데이터 없을 시 에러 , request.POST.get() >> 데이터 없을 시 null처리
    name = request.POST.get('name')     
    major = request.POST.get('major')     
    grade = request.POST.get('grade')     
    age = request.POST.get('age')     
    gender = request.POST.get('gender')     
    print('데이터 정보 :',name,major,grade,age,gender)
    
    qs = Student(name=name,major=major,grade=grade,age=age,gender=gender)
    qs.save()
    
    # 앱 이름 링크 / url 링크
    return redirect('students:list')    # redirect(app_name:list) >> app_name 사용 시 유지보수 용이

    # return HttpResponseRedirect(reverse('students:list'))
    # return render(request,'students/write.html')