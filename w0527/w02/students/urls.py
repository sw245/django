from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('list/',views.list,name='list'),
    path('write/',views.write,name='write'),
]