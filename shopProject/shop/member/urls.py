from django.urls import path
from . import views

app_name = 'member'

urlpatterns = [
    path('login/',views.login,name='login'),
    path('step01/',views.step01,name='step01'),
    # path('logout/',views.logout,name='logout'),
    path('emailSend/',views.emailSend,name='emailSend'),
    # path('confirmChk/',views.confirmChk,name='confirmChk'),
]