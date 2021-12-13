from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.loginpage),
    path('home', views.home),
    path('login/', views.loginpage),
    path('analytics/', views.analytics),

]