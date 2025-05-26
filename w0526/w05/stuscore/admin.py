from django.contrib import admin
from .models import Stuscore

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['no','name','total']

admin.site.register(Stuscore)