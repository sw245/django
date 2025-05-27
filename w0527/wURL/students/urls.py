from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('result/',views.result,name='result'),
    path('result2/<str:name>/<str:id>/<str:pw>/',views.result2,name='result2'),
]

