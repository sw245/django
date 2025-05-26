from django.shortcuts import render

# Create your views here.
def event1(request):
    return render(request, 'event1.html')