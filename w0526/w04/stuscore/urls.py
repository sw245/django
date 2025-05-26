from django.urls import path
from . import views

app_name = 'stuscore'

urlpatterns = [
    path('list_s/',views.list_s,name='list_s')
]