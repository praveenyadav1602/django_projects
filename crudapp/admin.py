from django.contrib import admin
from django.db import models
from .models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    class Meta:
        model = Student
        list_display = ['name','roll','email']

admin.site.register(Student,StudentAdmin)        