from django.shortcuts import render

# Main page
def index(request):
    return render(request, 'index.html')

# User related pages
def user_login(request):
    return render(request, 'login.html')

def user_register(request):
    return render(request, 'register.html')

def user_forgot_password(request):
    return render(request, 'forgotPassword.html')

# Instructor related pages
def instructor_login(request):
    return render(request, 'instructor_login.html')

def instructor_register(request):
    return render(request, 'instructor_register.html')

def instructor_forgot_password(request):
    return render(request, 'instructor_forgotPassword.html')

# College related pages
def college_login(request):
    return render(request, 'college_login.html')

def college_register(request):
    return render(request, 'college_register.html')

def college_forgot_password(request):
    return render(request, 'college_forgot-password.html')

# Organisation related pages
def organisation_login(request):
    return render(request, 'organisation_login.html')

def organisation_register(request):
    return render(request, 'organisation_register.html')

def organisation_forgot_password(request):
    return render(request, 'organisation_forgotPassword.html')

# Admin related pages
def admin_login(request):
    return render(request, 'admin_login.html')

def admin_register(request):
    return render(request, 'admin_register.html')

def admin_forgot_password(request):
    return render(request, 'admin_forgotpassword.html')