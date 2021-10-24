from django.contrib import admin
from django.db.models.base import Model
from .models import Profile
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = Profile
        list_display = ['user','token','varify']

admin.site.register(Profile,ProfileAdmin)        