from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('list/',views.list,name='list'),   # list url >> list 함수 호출
    path('write/',views.write,name='write'),
    path('write2/',views.write2,name='write2'),
]