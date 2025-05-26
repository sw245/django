from django.urls import path
from . import views

app_name = 'event'

urlpatterns = [
    path('1/',views.event1,name='event1')
]