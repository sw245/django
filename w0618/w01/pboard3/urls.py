from django.urls import path
from . import views

app_name = 'pboard3'

urlpatterns = [
    path('list_p3/', views.list_p3,name='list_p3'),
    path('view/<str:movieCd>/', views.view,name='view'),
]


