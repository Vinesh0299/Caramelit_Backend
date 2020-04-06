from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(response):
    return render(response, 'index.html')

def user_login(response):
    return render(response, 'login.html')

def user_register(response):
    return render(response, 'register.html')

def user_forgot_password(response):
    return render(response, 'forgotPassword.html')