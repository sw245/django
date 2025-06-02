from django.urls import path
from . import views

app_name = 'member'

urlpatterns = [
    path('login/',views.login,name='login'),
    path('logout/',views.login,name='login'),
    path('submit/',views.submit,name='submit'),
    path('join01/',views.join01,name='join01'),     # 약관 동의
    path('join02/',views.join02,name='join02'),     # 회원가입페이지
    path('join03/',views.join03,name='join03'),     # 가입완료
]
