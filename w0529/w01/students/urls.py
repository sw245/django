from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('list/',views.list,name='list'),
    path('write/',views.write,name='write'),
    path('write_ok/',views.write_ok,name='write_ok'),
    path('view/<int:no>/',views.view,name='view'),
    path('update/<int:no>/',views.update,name='update'),
    path('update_ok/',views.update_ok,name='update_ok'),
    path('delete/<int:no>/',views.delete,name='delete'),
]

