from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('list/',views.list,name='list'),
    path('view/<int:no>/',views.view,name='view'),
    path('write/',views.write,name='write'),
]