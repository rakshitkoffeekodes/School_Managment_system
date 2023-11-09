from django.db import models


# Create your models here.

class register(models.Model):
    admin_first_name = models.CharField(max_length=100)
    admin_last_name = models.CharField(max_length=100)
    admin_email = models.CharField(max_length=100)
    admin_password = models.CharField(max_length=50)

    def __str__(self):
        return self.admin_first_name + " " + self.admin_last_name


class log(models.Model):
    admin_login_time = models.DateTimeField()

    def __str__(self):
        return self.admin_login_time


class profile(models.Model):
    admin_profile_name = models.CharField(max_length=200)
    admin_profile_address = models.TimeField()
    admin_profile_gender = models.CharField(max_length=20)
    admin_profile_M_number = models.CharField(max_length=20)
    admin_profile_DOB = models.DateField()
    admin_profile_status = models.CharField(max_length=30)

    def __str__(self):
        return self.admin_profile_name


class add_student(models.Model):
    student_name = models.CharField(max_length=200)
    student_address = models.TextField()
    student_course = models.CharField(max_length=50)
    student_DOB = models.DateField()

    def __str__(self):
        return self.student_name + " " + self.student_course


class add_parent(models.Model):
    parents_name = models.CharField(max_length=200)
    student_name = models.CharField(max_length=200)
    parents_address = models.TextField()
    parents_gender = models.CharField(max_length=20)

    def __str__(self):
        return self.parents_name + " " + self.student_name


class add_faculty(models.Model):
    faculty_name = models.CharField(max_length=200)
    faculty_address = models.TextField()
    faculty_position = models.CharField(max_length=100)
    faculty_gender = models.CharField(max_length=20)
    faculty_exprience = models.CharField(max_length=10)
    faculty_subject = models.CharField(max_length=20)
    faculty_class = models.CharField(max_length=10)


class add_course(models.Model):
    course_name = models.CharField(max_length=20)
    course_of_subjects = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name


class time_table(models.Model):
    school_std = models.CharField(max_length=30)
    school_start = models.TimeField()
    school_end = models.TimeField()
    school_day1 = models.CharField(max_length=20)
    day1_subject = models.TextField()
    school_day2 = models.CharField(max_length=20)
    day2_subject = models.TextField()
    school_day3 = models.CharField(max_length=20)
    day3_subject = models.TextField()
    school_day4 = models.CharField(max_length=20)
    day4_subject = models.TextField()
    school_day5 = models.CharField(max_length=20)
    day5_subject = models.TextField()
    school_day6 = models.CharField(max_length=20)
    day6_subject = models.TextField()


class exam_timetable(models.Model):
    exam_std = models.CharField(max_length=50)
    exam_date = models.CharField(max_length=200)
    exam_subject = models.CharField(max_length=200)
    exam_time = models.TimeField()

    def __str__(self):
        return self.exam_std


class event_activity_notice(models.Model):
    E_A_Name = models.CharField(max_length=50)
    E_A_Notice = models.TextField()
    E_A_Date_Time = models.DateTimeField()

    def __str__(self):
        return self.E_A_Name

class Notice(models.Model):
    Notice_Name = models.CharField(max_length=50)
    Name = models.CharField(max_length=30)
    Notice = models.TextField()

