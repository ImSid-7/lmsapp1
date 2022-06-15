from django.contrib import admin
from django.urls import path
from LMSapp import views

urlpatterns = [
    path("", views.index, name='LMS'),
    path("register/", views.register, name="register"),
    path("register/home/", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("resources/", views.resources, name="resources"),

]