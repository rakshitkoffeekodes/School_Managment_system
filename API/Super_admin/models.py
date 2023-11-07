from django.db import models


# Create your models here.

class Suprt_admin_register(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Super_admin_login(models.Model):
    login_email = models.CharField(max_length=500)
    login_password = models.CharField(max_length=200)
    login_datetime = models.DateTimeField(null=True)

    def __str__(self):
        return self.login_email


class Super_admin_profile(models.Model):
    profile_name = models.CharField(max_length=500)
    profile_address = models.CharField(max_length=500)
    profile_gender = models.CharField(max_length=100)
    profile_M_number = models.IntegerField(default=0)
    profile_DOB = models.DateField()
    profile_status = models.CharField(max_length=200)

    def __str__(self):
        return self.profile_name


class Super_admin_add_student(models.Model):
    student_name = models.CharField(max_length=500)
    student_address = models.TextField()
    student_course = models.CharField(max_length=500)
    student_DOB = models.DateField()

    def __str__(self):
        return self.student_name + " " + self.student_course

class Super_admin_add_faculty(models.Model):
    faculty_name = models.CharField(max_length=500)
    faculty_position = models.CharField(max_length=200)
    faculty_address = models.CharField(max_length=500)
    faculty_exprience = models.CharField(max_length=200)
    faculty_subjects = models.CharField(max_length=200)
    faculty_class = models.CharField(max_length=300)

    def __str__(self):
        return self.faculty_name + " " + self.faculty_position

class Super_admin_add_admin(models.Model):
    admin_name = models.CharField(max_length=500)
    admin_address = models.CharField(max_length=500)
    admin_DOB = models.DateField()
    admin_exprince = models.CharField(max_length=200)

    def __str__(self):
        return self.admin_name

class Super_admin_add_event_activite(models.Model):
    E_A_name = models.CharField(max_length=300)
    E_A_Notice = models.TextField()

    def __str__(self):
        return self.E_A_name

class Super_admin_fees_notice(models.Model):
    Student_name = models.CharField(max_length=100)
    fees_notice = models.TextField()

    def __str__(self):
        return self.Student_name

class Super_admin_time_table(models.Model):
    table_days = models.CharField(max_length=200)
    table_time = models.TimeField()
    table_subject = models.TextField()
    table_course = models.CharField(max_length=100)

    def __str__(self):
        return self.table_course

