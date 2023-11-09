from django.db import models


# Create your models here.

class register(models.Model):
    faculty_first_name = models.CharField(max_length=100)
    faculty_last_name = models.CharField(max_length=100)
    faculty_email = models.CharField(max_length=100)
    faculty_password = models.CharField(max_length=50)

    def __str__(self):
        return self.faculty_first_name + " " + self.faculty_last_name


class login(models.Model):
    faculty_email = models.CharField(max_length=100)
    faculty_password = models.CharField(max_length=50)
    faculty_login_time = models.TimeField()

    def __str__(self):
        return self.faculty_email


class profile(models.Model):
    faculty_name = models.CharField(max_length=100)
    faculty_address = models.TextField()
    faculty_position = models.CharField(max_length=100)
    faculty_gender = models.CharField(max_length=50)
    faculty_M_Number = models.CharField(max_length=15)
    faculty_status = models.CharField(max_length=20)

    def __str__(self):
        return self.faculty_name + " " + self.faculty_position


class create_result(models.Model):
    student_name = models.CharField(max_length=100)
    student_std = models.CharField(max_length=20)
    result_subjects = models.TextField()
    result_marks = models.TextField()
    result_total_marks = models.CharField(max_length=10)
    returlt_persantag = models.CharField(max_length=10)

    def __str__(self):
        return self.student_name + " " + self.student_std + " " + self.returlt_persantag


class Assignment(models.Model):
    std = models.CharField(max_length=20)
    upload_assignment = models.FilePathField(null=True)

    def __str__(self):
        return self.std + "Assignment"


class Projetc(models.Model):
    std = models.CharField(max_length=20)
    upload_projects = models.FilePathField(null=True)

    def __str__(self):
        return self.std + "Projects"


class attendens(models.Model):
    std = models.CharField(max_length=20)
    student_name = models.CharField(max_length=100)
    student_attendens = models.BooleanField(null=True)

    def __str__(self):
        return self.std + " student name " + self.student_name


class reprot_admin(models.Model):
    faculty_name = models.CharField(max_length=100)
    faculty_report = models.TextField()

    def __str__(self):
        return self.faculty_name
