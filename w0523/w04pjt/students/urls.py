from django.urls import path,include
from . import views

app_name = 'students'
urlpatterns = [
    path('list/', view=views.list, name='list'),
    path('view/', view=views.view, name='view'),
    path('write/', view=views.write, name='write'),
    path('delete/', view=views.delete, name='delete'),
]