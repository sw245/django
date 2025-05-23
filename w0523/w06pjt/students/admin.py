from django.contrib import admin
from students.models import Students

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','major','age']
    

admin.site.register(Students,StudentAdmin)