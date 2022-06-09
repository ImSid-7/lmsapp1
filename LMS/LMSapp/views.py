from django.shortcuts import render, redirect
from django import forms
from .forms import RegisterForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import os


# Create your views here.
def index(request):
    return render(request, 'index.html')
def home(request):
    return render(request, 'index.html')
def resources(request):
    path="C:\\django\\LMS\\static\\"  
    video_list =os.listdir(path)   
    return render(request,'resources.html', {'videos': video_list})
def register(response):
    if response.method == "POST" :
        form= RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('/home')
    else:
        form =RegisterForm()
    return render(response,"register.html",{"form":form})