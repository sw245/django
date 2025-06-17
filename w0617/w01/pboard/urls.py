from django.urls import path
from . import views

app_name = 'pboard'

urlpatterns = [
    path('list_p/', views.list_p,name='list_p'),
    path('view/<str:galContentId>/', views.view,name='pboard/view.html'),
]


