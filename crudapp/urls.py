
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    
    path('',views.index,name='index'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update')
    
]

