from django.core import validators
from django import forms
from django.db.models import fields
from .models import Student

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','roll','email']
        