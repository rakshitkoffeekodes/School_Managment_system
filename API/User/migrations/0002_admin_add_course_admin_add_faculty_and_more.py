# Generated by Django 4.2.2 on 2023-11-08 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_add_course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=20)),
                ('course_of_subjects', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Admin_add_faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=200)),
                ('faculty_address', models.TextField()),
                ('faculty_position', models.CharField(max_length=100)),
                ('faculty_gender', models.CharField(max_length=20)),
                ('faculty_exprience', models.CharField(max_length=10)),
                ('faculty_subject', models.CharField(max_length=20)),
                ('faculty_class', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Admin_event_activity_notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('E_A_Name', models.CharField(max_length=50)),
                ('E_A_Notice', models.TextField()),
                ('E_A_Date_Time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Admin_exam_timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_std', models.CharField(max_length=50)),
                ('exam_date', models.CharField(max_length=200)),
                ('exam_subject', models.CharField(max_length=200)),
                ('exam_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Admin_Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Notice_Name', models.CharField(max_length=50)),
                ('Name', models.CharField(max_length=30)),
                ('Notice', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Admin_time_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_std', models.CharField(max_length=30)),
                ('school_start', models.TimeField()),
                ('school_end', models.TimeField()),
                ('school_day1', models.CharField(max_length=20)),
                ('day1_subject', models.TextField()),
                ('school_day2', models.CharField(max_length=20)),
                ('day2_subject', models.TextField()),
                ('school_day3', models.CharField(max_length=20)),
                ('day3_subject', models.TextField()),
                ('school_day4', models.CharField(max_length=20)),
                ('day4_subject', models.TextField()),
                ('school_day5', models.CharField(max_length=20)),
                ('day5_subject', models.TextField()),
                ('school_day6', models.CharField(max_length=20)),
                ('day6_subject', models.TextField()),
            ],
        ),
    ]