from django.urls import path,include
from . import views


app_name = ''

urlpatterns = [
    path('', view=views.home, name='home'),
]
