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

urlpatterns = [
    path('admin/', admin.site.urls),
    # Main page
    path('', loginviews.index, name="index"),
    # User oriented pages
    path('user/login', loginviews.user_login, name='user_login'),
    path('user/register', loginviews.user_register, name='user_register'),
    path('user/forgot-password', loginviews.user_forgot_password, name='user_forgot_password'),
    path('user/logout', loginviews.logout, name='user_logout'),
    # Instructor oriented pages
    path('instructor/instructor_login', loginviews.instructor_login, name='instructor_login'),
    path('instructor/instructor_register', loginviews.instructor_register, name='instructor_register'),
    path('instructor/instructor_forgot-password', loginviews.instructor_forgot_password, name='instructor_forgot_password'),
    path('instructor/logout', loginviews.instructor_logout, name='instructor_logout'),
    # College oriented pages
    path('college/college_login', loginviews.college_login, name='college_login'),
    path('college/college_register', loginviews.college_register, name='college_register'),
    path('college/college_forgot-password', loginviews.college_forgot_password, name='college_forgot_password'),
    path('college/logout', loginviews.college_logout, name='college_logout'),
    # Organisation oriented pages
    path('organisation/organisation_login', loginviews.organisation_login, name='organisation_login'),
    path('organisation/organisation_register', loginviews.organisation_register, name='organisation_register'),
    path('organisation/organisation_forgot-password', loginviews.organisation_forgot_password, name='organisation_forgot_password'),
    path('organisation/logout', loginviews.organisation_logout, name='organisation_logout'),
    # Admin oriented pages
    path('admin/admin_login', loginviews.admin_login, name='admin_login'),
    path('admin/admin_register', loginviews.admin_register, name='admin_register'),
    path('admin/admin_forgot-password', loginviews.admin_forgot_password, name='admin_forgot_password'),
    path('admin/admin_successLogin', loginviews.admin_successLogin, name='admin_successLogin'),
    path('admin/logout', loginviews.admin_logout, name='admin_logout'),
]
