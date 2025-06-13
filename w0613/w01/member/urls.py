from django.urls import path
from . import views

app_name = 'member'

urlpatterns = [
    path('mlist/',views.mlist,name='mlist'),
]
