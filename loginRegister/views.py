from django.shortcuts import render, redirect
from .models import studentUser, adminUser, instructor, college, organisation
import hashlib
from django.http import HttpResponse

salt = b'vB\\xa6\\xc4M(\\x07\\xbd\\xcc\\x00\\xf5*\\x93\\xb9\\xdb{\\xa4)\\xa4\\xff\\xe3_Z\\x87<\\xc4\\xcc\\x93\\xe5\\xa3\\x8f\\xdb'

# Main page
def index(request):
    return render(request, 'index.html')

# User related pages
def user_login(request):
    try:
        if len(request.COOKIES.get('username')) > 0 and request.COOKIES.get('type') == 'student':
            return redirect('/user/user_successLogin')
    except Exception as e:
        pass
    if request.method == 'POST':
        global salt
        email = request.POST.get('email')
        password = request.POST.get('password')
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        try:
            student = studentUser.objects.get(email=email)
            if student.password == str(key):
                response = redirect('/user/user_successLogin')
                response.set_cookie('username', email)
                response.set_cookie('type', 'student')
                return response
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

def user_successLogin(request):
    return render(request, 'successLogin.html')

def logout(request):
    response = redirect('/user/user_login')
    response.set_cookie('username', None)
    response.set_cookie('type', None)
    return response

# Instructor related pages
def instructor_login(request):
    try:
        if len(request.COOKIES.get('username')) > 0 and request.COOKIES.get('type') == 'instructor':
            return redirect('/instructor/instructor_successLogin')
    except Exception as e:
        pass
    if request.method == 'POST':
        global salt
        email = request.POST.get('email')
        password = request.POST.get('password')
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        try:
            instructor = instructor.objects.get(email=email)
            if instructor.password == str(key):
                response = redirect('/instructor/instructor_successLogin')
                response.set_cookie('username', email)
                response.set_cookie('type', 'instructor')
                return response
            else:
                state = 2
                return render(request, 'instructor_login.html', {'state': state})
        except Exception as e:
            state = 3
            return render(request, 'instructor_login.html', {'state': state})
    return render(request, 'instructor_login.html')

def instructor_register(request):
    return render(request, 'instructor_register.html')

def instructor_forgot_password(request):
    return render(request, 'instructor_forgotPassword.html')

def instructor_successLogin(request):
    return render(request, 'instructor_successLogin.html')

def instructor_logout(request):
    response = redirect('/instructor/instructor_login')
    response.set_cookie('username', None)
    response.set_cookie('type', None)
    return response

# College related pages
def college_login(request):
    try:
        if len(request.COOKIES.get('username')) > 0 and request.COOKIES.get('type') == 'college':
            return redirect('/college/college_successLogin')
    except Exception as e:
        pass
    if request.method == 'POST':
        global salt
        email = request.POST.get('email')
        password = request.POST.get('password')
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        try:
            college = college.objects.get(email=email)
            if college.password == str(key):
                response = redirect('/college/college_successLogin')
                response.set_cookie('username', email)
                response.set_cookie('type', 'college')
                return response
            else:
                state = 2
                return render(request, 'college_login.html', {'state': state})
        except Exception as e:
            state = 3
            return render(request, 'college_login.html', {'state': state})
    return render(request, 'college_login.html')

def college_register(request):
    return render(request, 'college_register.html')

def college_forgot_password(request):
    return render(request, 'college_forgot-password.html')

def college_successLogin(request):
    return render(request, 'college_successLogin.html')

def college_logout(request):
    response = redirect('/college/college_login')
    response.set_cookie('username', None)
    response.set_cookie('type', None)
    return response

# Organisation related pages
def organisation_login(request):
    try:
        if len(request.COOKIES.get('username')) > 0 and request.COOKIES.get('type') == 'organisation':
            return redirect('/organisation/organisation_successLogin')
    except Exception as e:
        pass
    if request.method == 'POST':
        global salt
        email = request.POST.get('email')
        password = request.POST.get('password')
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        try:
            organisation = organisation.objects.get(email=email)
            if organisation.password == str(key):
                response = redirect('/organisation/organisation_successLogin')
                response.set_cookie('username', email)
                response.set_cookie('type', 'organisation')
                return response
            else:
                state = 2
                return render(request, 'organisation_login.html', {'state': state})
        except Exception as e:
            state = 3
            return render(request, 'organisation_login.html', {'state': state})
    return render(request, 'organisation_login.html')

def organisation_register(request):
    return render(request, 'organisation_register.html')

def organisation_forgot_password(request):
    return render(request, 'organisation_forgotPassword.html')

def organisation_successLogin(request):
    return render(request, 'organisation_successLogin.html')

def organisation_logout(request):
    response = redirect('/organisation/organisation_login')
    response.set_cookie('username', None)
    response.set_cookie('type', None)
    return response

# Admin related pages
def admin_login(request):
    try:
        if len(request.COOKIES.get('username')) > 0 and request.COOKIES.get('type') == 'admin':
            return redirect('/admin/admin_successLogin')
    except Exception as e:
        pass
    state = 1
    if request.method == 'POST':
        global salt
        email = request.POST.get('email')
        password = request.POST.get('password')
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        try:
            admin = adminUser.objects.get(email=email)
            if admin.password == str(key):
                response = redirect('/admin/admin_successLogin')
                response.set_cookie('username', email)
                response.set_cookie('type', 'admin')
                return response
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

def admin_logout(request):
    response = redirect('/admin/admin_login')
    response.set_cookie('username', None)
    response.set_cookie('type', None)
    return response