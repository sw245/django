from django.shortcuts import render

# Create your views here.
def result(request):
    name = request.GET.get('name')
    id = request.GET.get('id')
    password = request.GET.get('password')
    context = {'name':name,'id':id,'password':password}
    return render(request,'result.html',context)

def result2(request,name,id,pw):
    context = {'name':name,'id':id,'pw':pw}
    return render(request,'result2.html',context)