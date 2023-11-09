from django.db import models

# Create your models here.

class register(models.Model):
    student_first_name = models.CharField(max_length=100)
    student_last_name = models.CharField(max_length=100)
    student_email = models.CharField(max_length=100)
    student_password = models.CharField(max_length=50)

    def __str__(self):
        return self.student_first_name + " " + self.student_last_name

class login(models.Model):
    student_email = models.CharField(max_length=100)
    student_password =models.CharField(max_length=50)
    student_login_time = models.DateTimeField()

    def __str__(self):
        return self.student_email

class profile(models.Model):
    student_name = models.CharField(max_length=100)
    student_address = models.TextField()
    student_email = models.CharField(max_length=50)
    student_course = models.CharField(max_length=20)
    student_DOB = models.DateField()

    def __str__(self):
        return self.student_name + " " + self.student_course

class upload_assignment(models.Model):
    student_name = models.CharField(max_length=100)
    student_std = models.CharField(max_length=20)
    student_assignment = models.FilePathField()

    def __str__(self):
        return self.student_name +" " + self.student_std


class upload_projects(models.Model):
    student_name = models.CharField(max_length=100)
    student_std = models.CharField(max_length=20)
    student_projects = models.FilePathField()

    def __str__(self):
        return self.student_name + " " + self.student_std

class reporting(models.Model):
    student_name = models.CharField(max_length=100)
    student_std = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    reporting = models.TextField()

    def __str__(self):
        return self.student_std + " " + self.student_name + " to " + self.name
