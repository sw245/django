from django.urls import path
from . import views

app_name = 'stuscore'

urlpatterns = [
    path('list/',views.list,name='list')
]

