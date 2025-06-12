from django.urls import path
from . import views

app_name = 'ajaxData'

urlpatterns = [
    path('bwrite/', views.bwrite, name='bwrite'),
]


