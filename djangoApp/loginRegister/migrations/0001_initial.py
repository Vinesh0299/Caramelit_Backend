# Generated by Django 2.2.12 on 2020-04-08 16:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='college',
            fields=[
                ('college_id', models.AutoField(primary_key=True, serialize=False)),
                ('college_name', models.CharField(max_length=100)),
                ('university_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.BigIntegerField()),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('skill_set', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('profileImg', models.CharField(max_length=100)),
                ('date_of_reg', models.DateTimeField(default=django.utils.timezone.now)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='instructor',
            fields=[
                ('instructor_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.BigIntegerField()),
                ('subjects', models.CharField(max_length=100)),
                ('job_type', models.CharField(max_length=8)),
                ('experience', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('profileImg', models.CharField(max_length=100)),
                ('date_of_reg', models.DateTimeField(default=django.utils.timezone.now)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='organisation',
            fields=[
                ('organisation_id', models.AutoField(primary_key=True, serialize=False)),
                ('organisation_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.BigIntegerField()),
                ('description', models.TextField()),
                ('profileImg', models.CharField(max_length=100)),
                ('date_of_reg', models.DateTimeField(default=django.utils.timezone.now)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='studentUser',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.BigIntegerField()),
                ('birth_date', models.DateTimeField()),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('college', models.CharField(max_length=100)),
                ('skill_set', models.CharField(max_length=100)),
                ('profileImg', models.CharField(max_length=100)),
                ('date_of_reg', models.DateTimeField(default=django.utils.timezone.now)),
                ('no_of_courses', models.IntegerField(default=0)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
