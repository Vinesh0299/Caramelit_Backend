from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Main page
def index(response):
    return render(response, 'index.html')

# User related pages
def user_login(response):
    return render(response, 'login.html')

def user_register(response):
    return render(response, 'register.html')

def user_forgot_password(response):
    return render(response, 'forgotPassword.html')

# Instructor related pages
def instructor_login(response):
    return render(response, 'instructor_login.html')

def instructor_register(response):
    return render(response, 'instructor_register.html')

def instructor_forgot_password(response):
    return render(response, 'instructor_forgotPassword.html')

# College related pages
def college_login(response):
    return render(response, 'college_login.html')

def college_register(response):
    return render(response, 'college_register.html')

def college_forgot_password(response):
    return render(response, 'college_forgot-password.html')

# Organisation related pages
def organisation_login(response):
    return render(response, 'organisation_login.html')

def organisation_register(response):
    return render(response, 'organisation_register.html')

def organisation_forgot_password(response):
    return render(response, 'organisation_forgotPassword.html')

# Admin related pages
def admin_login(response):
    return render(response, 'admin_login.html')

def admin_register(response):
    return render(response, 'admin_register.html')

def admin_forgot_password(response):
    return render(response, 'admin_forgotpassword.html')