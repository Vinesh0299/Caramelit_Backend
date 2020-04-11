from django.shortcuts import render, redirect
from .models import studentUser, adminUser, instructor, college, organisation
import hashlib

salt = b'vB\\xa6\\xc4M(\\x07\\xbd\\xcc\\x00\\xf5*\\x93\\xb9\\xdb{\\xa4)\\xa4\\xff\\xe3_Z\\x87<\\xc4\\xcc\\x93\\xe5\\xa3\\x8f\\xdb'

# Main page
def index(request):
    return render(request, 'index.html')

# User related pages
def user_login(request):
    if request.method == 'POST':
        global salt
        email = request.POST.get('email')
        password = request.POST.get('password')
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        try:
            student = studentUser.objects.get(email=email)
            if student.password == str(key):
                state = 1
                return redirect('/user/successLogin')
            else:
                state = 2
                return render(request, 'login.html', {'state': state})
        except Exception as e:
            state = 3
            return render(request, 'login.html', {'state': state})
    return render(request, 'login.html')

def user_register(request):
    return render(request, 'register.html')

def user_forgot_password(request):
    return render(request, 'forgotPassword.html')

# Instructor related pages
def instructor_login(request):
    if request.method == 'POST':
        global salt
        email = request.POST.get('email')
        password = request.POST.get('password')
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        try:
            instructor = instructor.objects.get(email=email)
            if instructor.password == str(key):
                return redirect('/instructor/instructor_successLogin')
            else:
                return redirect('/instructor/instructor_login')
        except Exception as e:
            return redirect('/instructor/instructor_login')
    return render(request, 'instructor_login.html')

def instructor_register(request):
    return render(request, 'instructor_register.html')

def instructor_forgot_password(request):
    return render(request, 'instructor_forgotPassword.html')

# College related pages
def college_login(request):
    if request.method == 'POST':
        global salt
        email = request.POST.get('email')
        password = request.POST.get('password')
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        try:
            college = college.objects.get(email=email)
            if college.password == str(key):
                return redirect('/college/college_successLogin')
            else:
                return redirect('/college/college_login')
        except Exception as e:
            return redirect('/college/college_login')
    return render(request, 'college_login.html')

def college_register(request):
    return render(request, 'college_register.html')

def college_forgot_password(request):
    return render(request, 'college_forgot-password.html')

# Organisation related pages
def organisation_login(request):
    if request.method == 'POST':
        global salt
        email = request.POST.get('email')
        password = request.POST.get('password')
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        try:
            organisation = organisation.objects.get(email=email)
            if organisation.password == str(key):
                return redirect('/organisation/organisation_successLogin')
            else:
                return redirect('/organisation/organisation_login')
        except Exception as e:
            return redirect('/organisation/organisation_login')
    return render(request, 'organisation_login.html')

def organisation_register(request):
    return render(request, 'organisation_register.html')

def organisation_forgot_password(request):
    return render(request, 'organisation_forgotPassword.html')

# Admin related pages
def admin_login(request):
    state = 1
    if request.method == 'POST':
        global salt
        email = request.POST.get('email')
        password = request.POST.get('password')
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        try:
            admin = adminUser.objects.get(email=email)
            if admin.password == str(key):
                state = 1
                return redirect('/admin/admin_successLogin')
            else:
                state = 2
                return render(request, 'admin_login.html', {'state': state})
        except Exception as e:
            state = 3
            return render(request, 'admin_login.html', {'state': state})
    return render(request, 'admin_login.html')

def admin_register(request):
    return render(request, 'admin_register.html')

def admin_forgot_password(request):
    return render(request, 'admin_forgotpassword.html')

def admin_successLogin(request):
    return render(request, 'admin_successLogin.html')