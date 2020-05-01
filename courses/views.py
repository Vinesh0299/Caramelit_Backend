from django.shortcuts import render
from .models import Course

# List all courses
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/courses.html', {'data' : courses})

# Course pages
def uicourses(request):
    return render(request, 'courses/course.html')

def backend(request):
    return render(request, 'courses/course.html')

def fullstack(request):
    return render(request, 'courses/course.html')

def functionaltesting(request):
    return render(request, 'courses/course.html')

def mobility(request):
    return render(request, 'courses/course.html')

def devops(request):
    return render(request, 'courses/course.html')

def datascience(request):
    return render(request, 'courses/course.html')

def cloud(request):
    return render(request, 'courses/course.html')

def cyber(request):
    return render(request, 'courses/course.html')

def digital(request):
    return render(request, 'courses/course.html')

def erp(request):
    return render(request, 'courses/course.html')

def it(request):
    return render(request, 'courses/course.html')

def itcertification(request):
    return render(request, 'courses/course.html')

def coreui(request):
    return render(request, 'courses/course.html')

def advancedui(request):
    return render(request, 'courses/course.html')

def angularjs(request):
    return render(request, 'courses/course.html')

def reactjs(request):
    return render(request, 'courses/course.html')

def vuejs(request):
    return render(request, 'courses/course.html')

def java(request):
    return render(request, 'courses/course.html')

def net(request):
    return render(request, 'courses/course.html')

def nodejs(request):
    return render(request, 'courses/course.html')

def coursedetails(request):
    return render(request, 'courses/course.html')