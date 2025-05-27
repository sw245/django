from django.urls import path
from . import views

app_name = ''

urlpatterns = [
    path('result/',views.result,name='result'),
]