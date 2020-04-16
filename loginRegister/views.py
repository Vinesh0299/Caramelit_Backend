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
            return redirect('/user/successLogin')
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
                response = redirect('/user/successLogin')
                response.set_cookie('username', email)
                response.set_cookie('type', 'student')
                return response
            else:
                return render(request, 'login.html', {'state': 2})
        except Exception as e:
            return render(request, 'login.html', {'state': 3})
    return render(request, 'login.html')

def user_register(request):
    if request.method == 'POST':
        global salt
        try:
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            phone = int(request.POST.get('phone'))
            birthDate = request.POST.get('birthDate')
            password = request.POST.get('password')
            country = request.POST.get('country')
            state = request.POST.get('state')
            college = request.POST.get('college')
            skills = request.POST.get('skill')
            student = studentUser.objects.filter(email=email)
            if len(student) > 0:
                return render(request, 'register.html', {'state': 3})
            student = studentUser(
                first_name=fname,
                last_name=lname,
                email=email,
                phone=phone,
                birth_date = birthDate,
                country=country,
                state=state,
                college=college,
                skill_set=skills,
                password=str(hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)),
            )
            student.save()
            return render(request, 'register.html', {'state': 2})
        except Exception as e:
            return render(request, 'register.html', {'state': 4})
    return render(request, 'register.html')

def user_forgot_password(request):
    return render(request, 'forgotPassword.html')

def user_successLogin(request):
    return render(request, 'successLogin.html')

def logout(request):
    response = redirect('/user/login')
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
            instructor1 = instructor.objects.get(email=email)
            if instructor1.password == str(key):
                response = redirect('/instructor/instructor_successLogin')
                response.set_cookie('username', email)
                response.set_cookie('type', 'instructor')
                return response
            else:
                return render(request, 'instructor_login.html', {'state': 2})
        except Exception as e:
            return render(request, 'instructor_login.html', {'state': 3})
    return render(request, 'instructor_login.html')

def instructor_register(request):
    if request.method == 'POST':
        global salt
        try:
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            phone = int(request.POST.get('phone'))
            password = request.POST.get('password')
            subject = request.POST.get('subject')
            jobtype = request.POST.get('jobtype')
            experience = request.POST.get('experience')
            description = request.POST.get('description')
            instructor1 = instructor.objects.filter(email=email)
            if len(instructor1) > 0:
                return render(request, 'instructor_register.html', {'state': 3})
            instructor1 = instructor(
                first_name=fname,
                last_name=lname,
                email=email,
                phone=phone,
                subjects=subject,
                job_type=jobtype,
                experience=experience,
                description=description,
                password=str(hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)),
            )
            instructor1.save()
            return render(request, 'instructor_register.html', {'state': 2})
        except Exception as e:
            return render(request, 'instructor_register.html', {'state': 4})
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
            college1 = college.objects.get(email=email)
            if college1.password == str(key):
                response = redirect('/college/college_successLogin')
                response.set_cookie('username', email)
                response.set_cookie('type', 'college')
                return response
            else:
                return render(request, 'college_login.html', {'state': 2})
        except Exception as e:
            return render(request, 'college_login.html', {'state': 3})
    return render(request, 'college_login.html')

def college_register(request):
    if request.method == 'POST':
        global salt
        try:
            collegename = request.POST.get('collegename')
            universityname = request.POST.get('universityname')
            email = request.POST.get('email')
            phone = int(request.POST.get('phone'))
            password = request.POST.get('password')
            country = request.POST.get('country')
            state = request.POST.get('state')
            skill = request.POST.get('skill')
            description = request.POST.get('description')
            college1 = college.objects.filter(email=email)
            if len(college1) > 0:
                return render(request, 'college_register.html', {'state': 3})
            college1 = college(
                college_name=collegename,
                university_name=universityname,
                email=email,
                phone=phone,
                country=country,
                state=state,
                skill_set=skill,
                description=description,
                password=str(hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)),
            )
            college1.save()
            return render(request, 'college_register.html', {'state': 2})
        except Exception as e:
            return render(request, 'college_register.html', {'state': 4})
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
            organisation1 = organisation.objects.get(email=email)
            if organisation1.password == str(key):
                response = redirect('/organisation/organisation_successLogin')
                response.set_cookie('username', email)
                response.set_cookie('type', 'organisation')
                return response
            else:
                return render(request, 'organisation_login.html', {'state': 2})
        except Exception as e:
            return render(request, 'organisation_login.html', {'state': 3})
    return render(request, 'organisation_login.html')

def organisation_register(request):
    if request.method == 'POST':
        global salt
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = int(request.POST.get('phone'))
            password = request.POST.get('password')
            description = request.POST.get('description')
            organisation1 = organisation.objects.filter(email=email)
            if len(organisation1) > 0:
                return render(request, 'organisation_register.html', {'state': 3})
            organisation1 = organisation(
                organisation_name=name,
                email=email,
                phone=phone,
                description=description,
                password=str(hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)),
            )
            organisation1.save()
            return render(request, 'organisation_register.html', {'state': 2})
        except Exception as e:
            return render(request, 'organisation_register.html', {'state': 4})
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
                return render(request, 'admin_login.html', {'state': 2})
        except Exception as e:
            return render(request, 'admin_login.html', {'state': 3})
    return render(request, 'admin_login.html')

def admin_register(request):
    global salt
    return render(request, 'admin_register.html')

def admin_forgot_password(request):
    return render(request, 'admin_forgotpassword.html')

def admin_successLogin(request):
    admin = adminUser.objects.get(email=request.COOKIES.get('username'))
    return render(request, 'admin_successLogin.html', {'name': admin.name})

def admin_logout(request):
    response = redirect('/admin/admin_login')
    response.set_cookie('username', None)
    response.set_cookie('type', None)
    return response

def user_list(request):
    users_data = studentUser.objects.all()
    return render(request, 'user_list.html', {'users': users_data})

def instructor_list(request):
    instructor_data = instructor.objects.all()
    return render(request, 'instructor_list.html', {'instructors': instructor_data})

def college_list(request):
    college_data = college.objects.all()
    return render(request, 'college_list.html', {'colleges': college_data})

def organisation_list(request):
    organisation_data = organisation.objects.all()
    return render(request, 'organisation_list.html', {'organisations': organisation_data})