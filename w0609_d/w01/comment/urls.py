from django.urls import path
from . import views

app_name = 'comment'
urlpatterns = [
    path('list/', views.list, name='list'),
]
