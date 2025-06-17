from django.urls import path
from . import views

app_name = 'chart'

urlpatterns = [
    path('chlist/', views.chlist,name='chlist'),
]


