from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('list/',views.list,name='list'),
    path('view/<int:bno>/',views.view,name='view'),
    path('write/',views.write,name='write'),
    path('update/<int:bno>/',views.update,name='update'),
]