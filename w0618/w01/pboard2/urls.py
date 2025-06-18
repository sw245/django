from django.urls import path
from . import views

app_name = 'pboard'

urlpatterns = [
    path('', views.list_p2,name='list_p2'),
]


