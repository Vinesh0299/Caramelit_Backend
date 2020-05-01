from django.shortcuts import render, redirect
from .models import Course, Course_resource, Course_category, Course_subcategory

# List all courses
def course_list(request):
    courses = Course.objects.all().values()
    return render(request, 'courses/courses.html', {'Courses' : courses})

def new_course(request):
    if request.method == 'POST':
        course_name = request.POST.get('coursename')
        category_name = request.POST.get('categoryname')
        subcategory_name = request.POST.get('subcategoryname')
        course_difficulty = request.POST.get('coursedifficulty')
        course_description = request.POST.get('coursedescription')
        resource = request.POST.get('numResource')
        response = redirect('/course/course_resource')
        course_cat = Course_category(category_name=category_name)
        course_cat.save()
        course_subcat = Course_subcategory(subcategory_name=subcategory_name, category=course_cat)
        course_subcat.save()
        course = Course(
            subcategory=course_subcat,
            subcategory_name=subcategory_name,
            category_name=category_name,
            course_name=course_name,
            course_difficulty=course_difficulty,
            course_description=course_description,
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
        course = Course.objects.filter(course_id=request.COOKIES.get('course_id'))[0]
        for resource in resources:
            Course_res = Course_resource(
                course=course,
                resourse_name=request.POST.get(resource+'_name'),
                resourse_link=request.POST.get(resource+'_link'),
                resourse_length=request.POST.get(resource+'_length'),
            )
            Course_res.save()
    return render(request, 'courses/course_resource.html', {'resources' : resources })

def edit_course(request, courseID):
    course = Course.objects.filter(course_id=courseID).values()
    if request.method == 'POST':
        course_name = request.POST.get('coursename')
        category_name = request.POST.get('categoryname')
        subcategory_name = request.POST.get('subcategoryname')
        course_difficulty = request.POST.get('coursedifficulty')
        course_description = request.POST.get('coursedescription')
        course.update(
            subcategory_name=subcategory_name,
            category_name=category_name,
            course_name=course_name,
            course_difficulty=course_difficulty,
            course_description=course_description,
        )
        return redirect('/course/list_course')
    return render(request, 'courses/edit_course.html', {'data' : course[0]})

def delete_course(request, courseID):
    Course.objects.filter(course_id=courseID).delete()
    return redirect('/course/list_course')

# Course pages
def uicourses(request):
    if request.COOKIES.get('username') == None or request.COOKIES.get('username') == 'None':
        return redirect('/user/login')
    uicourse = Course.objects.filter(course_id=2)
    uicourse_resource = Course_resource.objects.filter(course=uicourse[0])
    similar = Course.objects.filter(category_name=uicourse[0].category_name)
    return render(request, 'courses/course.html', {'course' : uicourse[0], 'course_resource' : uicourse_resource, 'similar' : similar, 'lectures' : len(uicourse_resource)})

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