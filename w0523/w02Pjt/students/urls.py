from django.urls import path,include
from . import views


app_name = 'students'

urlpatterns = [
    path('list/',views.list,name='list'),       # 학생 전체 리스트
    path('view/',views.view,name='view'),       # 학생 상세 페이지
    path('write/',views.write,name='write'),    # 학생 입력 페이지
    path('delete/',views.delete,name='delete'), # 학생 삭제 페이지
]