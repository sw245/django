from django.contrib import admin
from .models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):       # admin 페이지에서 테이블 표기 시 보이는 컬럼 추가
    list_display = ['name','major','grade']

admin.site.register(Student,StudentAdmin)