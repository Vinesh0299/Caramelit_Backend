from django.db import models
from django.utils import timezone

# Create your models here.
class studentUser(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.BigIntegerField()
    birth_date = models.DateTimeField()
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    skill_set = models.CharField(max_length=100)
    profileImg = models.CharField(max_length=100, default='photo.jpg')
    date_of_reg = models.DateTimeField(default=timezone.now)
    no_of_courses = models.IntegerField(default=0)
    password = models.CharField(max_length=100)

class instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.BigIntegerField()
    subjects = models.CharField(max_length=100)
    job_type = models.CharField(max_length=8)
    experience = models.CharField(max_length=100)
    description = models.TextField()
    profileImg = models.CharField(max_length=100, default='photo.jpg')
    date_of_reg = models.DateTimeField(default=timezone.now)
    password = models.CharField(max_length=100)

class college(models.Model):
    college_id = models.AutoField(primary_key=True)
    college_name = models.CharField(max_length=100)
    university_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.BigIntegerField()
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    skill_set = models.CharField(max_length=100)
    description = models.TextField()
    profileImg = models.CharField(max_length=100, default='photo.jpg')
    date_of_reg = models.DateTimeField(default=timezone.now)
    password = models.CharField(max_length=100)

class organisation(models.Model):
    organisation_id = models.AutoField(primary_key=True)
    organisation_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.BigIntegerField()
    description = models.TextField()
    profileImg = models.CharField(max_length=100, default='photo.jpg')
    date_of_reg = models.DateTimeField(default=timezone.now)
    password = models.CharField(max_length=100)