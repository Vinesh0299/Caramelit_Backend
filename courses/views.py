from django.shortcuts import render, redirect
from .models import Course, Course_resource, Course_category, Course_subcategory

# List all courses
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/courses.html', {'data' : courses})

def new_course(request):
    if request.method == 'POST':
        course_name = request.POST.get('coursename')
        category_name = request.POST.get('categoryname')
        subcategory_name = request.POST.get('subcategoryname')
        course_difficulty = request.POST.get('coursedifficulty')
        resource = request.POST.get('numResource')
        response = redirect('/course/course_resource')
        course_cat = Course(category_name=category_name)
        course_cat.save()
        course_subcat = Course_subcategory(subcategory_name=subcategory_name, category=course_cat.category_id)
        course_subcat.save()
        course = Course(
            subcategory=course_subcat.subcategory_id,
            subcategory_name=subcategory_name,
            category_name=category_name,
            course_name=course_name,
            course_difficulty=course_difficulty,
        )
        course.save()
        resources = []
        for i in range(int(resource)):
            resources.append('Resource '+str(i+1))
        response.set_cookie('resources', resources)
        response.set_cookie('course_id', course.course_id)
        return response
    return render(request, 'courses/new_course.html')

def course_resource(request):
    resources = request.COOKIES.get('resources')
    resources = resources[1:-1].replace("'", "").split(',')
    if request.method == 'POST':
        res = len(resources)
        for resource in resources:
            Course_res = Course_resource(
                course=int(request.COOKIES.get('course_id')),
                resourse_name=request.POST.get(resource+'_name'),
                resourse_link=request.POST.get(resource+'_link'),
                resource_length=request.POST.get(resource+'_length'),
            )
            Course_res.save()
    return render(request, 'courses/course_resource.html', {'resources' : resources })

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