from django.urls import path
from . import views

app_name = 'kakao'

urlpatterns = [
    path('oauth/', views.oauth,name='oauth'),
]


