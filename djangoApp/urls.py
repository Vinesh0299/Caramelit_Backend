"""djangoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import loginRegister.views as loginviews
import staticHome.views as staticviews
import courses.views as courseviews

urlpatterns = [
    path('admin/', admin.site.urls),
    # Main page
    path('', staticviews.index, name="index"),
    path('aboutus', staticviews.aboutus, name="aboutus"),
    path('consortium', staticviews.consortium, name="consortium"),
    path('academy', staticviews.academy, name="academy"),
    path('products', staticviews.products, name="products"),
    # Contact forms
    path('contact/contactform', staticviews.contactform, name="contactform"),
    path('contact/academycontact', staticviews.academycontact, name="academycontact"),
    path('contact/consortiumcontact', staticviews.consortiumcontact, name="consortiumcontact"),
    # User oriented pages
    path('user/login', loginviews.user_login, name='user_login'),
    path('user/register', loginviews.user_register, name='user_register'),
    path('user/forgot-password', loginviews.user_forgot_password, name='user_forgot_password'),
    path('user/successLogin', loginviews.user_successLogin, name='user_successLogin'),
    path('user/logout', loginviews.logout, name='user_logout'),
    path('user/successPasswordReset', loginviews.successPasswordReset, name='success_password_reset'),
    # Instructor oriented pages
    path('instructor/instructor_login', loginviews.instructor_login, name='instructor_login'),
    path('instructor/instructor_register', loginviews.instructor_register, name='instructor_register'),
    path('instructor/instructor_forgot-password', loginviews.instructor_forgot_password, name='instructor_forgot_password'),
    path('instructor/instructor_successLogin', loginviews.instructor_successLogin, name='instructor_successLogin'),
    path('instructor/logout', loginviews.instructor_logout, name='instructor_logout'),
    # College oriented pages
    path('college/college_login', loginviews.college_login, name='college_login'),
    path('college/college_register', loginviews.college_register, name='college_register'),
    path('college/college_forgot-password', loginviews.college_forgot_password, name='college_forgot_password'),
    path('college/college_successLogin', loginviews.college_successLogin, name='college_successLogin'),
    path('college/logout', loginviews.college_logout, name='college_logout'),
    # Organisation oriented pages
    path('organisation/organisation_login', loginviews.organisation_login, name='organisation_login'),
    path('organisation/organisation_register', loginviews.organisation_register, name='organisation_register'),
    path('organisation/organisation_forgot-password', loginviews.organisation_forgot_password, name='organisation_forgot_password'),
    path('organisation/organisation_successLogin', loginviews.organisation_successLogin, name='organisation_successLogin'),
    path('organisation/logout', loginviews.organisation_logout, name='organisation_logout'),
    # Admin oriented pages
    path('admin/admin_login', loginviews.admin_login, name='admin_login'),
    path('admin/admin_register', loginviews.admin_register, name='admin_register'),
    path('admin/admin_forgot-password', loginviews.admin_forgot_password, name='admin_forgot_password'),
    path('admin/admin_successLogin', loginviews.admin_successLogin, name='admin_successLogin'),
    path('admin/logout', loginviews.admin_logout, name='admin_logout'),
    path('user/user_list', loginviews.user_list, name='user_list'),
    path('instructor/instructor_list', loginviews.instructor_list, name='instructor_list'),
    path('college/college_list', loginviews.college_list, name='college_list'),
    path('organisation/organisation_list', loginviews.organisation_list, name='organisation_list'),
    path('course/list_course', courseviews.course_list, name="course_list"),
    # Industries related pages
    path('industries/automotive', staticviews.automotive, name="automotive"),
    path('industries/communication', staticviews.communication, name="communication"),
    path('industries/lifescience', staticviews.lifescience, name="lifescience"),
    path('industries/banking', staticviews.banking, name="banking"),
    path('industries/consumer', staticviews.consumer, name="consumer"),
    path('industries/travel', staticviews.travel, name="travel"),
    # Insights related pages
    path('insights/artificial', staticviews.artificial, name="artificial"),
    path('insights/blockchain', staticviews.blockchain, name="blockchain"),
    path('insights/iot', staticviews.iot, name="iot"),
    path('insights/futureworkforce', staticviews.futureworkforce, name="futureworkforce"),
    path('insights/cloudcomputing', staticviews.cloudcomputing, name="cloudcomputing"),
    path('insights/datascience', staticviews.datascience, name="datascience"),
    # Business related pages
    path('business/strategy', staticviews.strategy, name="strategy"),
    path('business/consulting', staticviews.consulting, name="consulting"),
    path('business/digital', staticviews.digital, name="digital"),
    path('business/technology', staticviews.technology, name="technology"),
    path('business/operations', staticviews.operations, name="operations"),
    path('business/Application', staticviews.Application, name="Application"),
    # Courses
    path('courses/uicourses', courseviews.uicourses, name="uicourses"),
    path('courses/backend', courseviews.backend, name="backend"),
    path('courses/fullstack', courseviews.fullstack, name="fullstack"),
    path('courses/functionaltesting', courseviews.functionaltesting, name="functionaltesting"),
    path('courses/mobility', courseviews.mobility, name="mobility"),
    path('courses/devops', courseviews.devops, name="devops"),
    path('courses/datascience', courseviews.datascience, name="datascience"),
    path('courses/cloud', courseviews.cloud, name="cloud"),
    path('courses/cyber', courseviews.cyber, name="cyber"),
    path('courses/digital', courseviews.digital, name="digital"),
    path('courses/erp', courseviews.erp, name="erp"),
    path('courses/it', courseviews.it, name="it"),
    path('courses/itcertification', courseviews.itcertification, name="itcertification"),
    path('courses/coursespage/coreui', courseviews.coreui, name="coreui"),
    path('courses/coursespage/advancedui', courseviews.advancedui, name="advancedui"),
    path('courses/coursespage/angularjs', courseviews.angularjs, name="angularjs"),
    path('courses/coursespage/reactjs', courseviews.reactjs, name="reactjs"),
    path('courses/coursespage/vuejs', courseviews.vuejs, name="vuejs"),
    path('courses/coursespage/java', courseviews.java, name="java"),
    path('courses/coursespage/.net', courseviews.net, name=".net"),
    path('courses/coursespage/nodejs', courseviews.nodejs, name="nodejs"),
    # Read more
    path('coursedetails', courseviews.coursedetails, name="coursedetails"),
]
