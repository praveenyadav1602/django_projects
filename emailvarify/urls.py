
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    
    path('',views.Home.as_view(),name='index'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('varify/<slug:token>',views.varify, name ='varify'),
    path('login/',views.loginf.as_view(), name ='login'),
    path('loginss/',views.loginss, name ='logins'),
    path('logout/',views.logoutt, name ='logoutt'),


    
]

