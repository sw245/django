from django.shortcuts import render

# Create your views here.
def result(request):
    id = request.POST.get('id')
    password = request.POST.get('password')
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    hobbys = request.POST.getlist('hobby')
    context = {'id':id,'password':password,'name':name,'gender':gender,'hobbys':hobbys}
    return render(request,'result.html',context)