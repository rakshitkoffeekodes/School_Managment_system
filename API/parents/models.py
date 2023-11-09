from django.db import models


# Create your models here.

class register(models.Model):
    parents_first_name = models.CharField(max_length=100)
    parents_last_name = models.CharField(max_length=100)
    parents_email = models.CharField(max_length=100)
    parents_password = models.CharField(max_length=50)

    def __str__(self):
        return self.parents_first_name + " " + self.parents_last_name


class login(models.Model):
    parents_email = models.CharField(max_length=100)
    parents_password = models.CharField(max_length=50)
    parents_login_date_time = models.DateTimeField()

    def __str__(self):
        return self.parents_email


class profile(models.Model):
    parents_name = models.CharField(max_length=100)
    parents_address = models.TextField()
    parents_email = models.CharField(max_length=100)
    parents_M_Number = models.CharField(max_length=15)
    student_name = models.CharField(max_length=100)
    parents_gender = models.CharField(max_length=20)
    parents_DOB = models.DateField()

    def __str__(self):
        return self.parents_name + " parents of " + self.student_name


class Report(models.Model):
    reporting_name = models.CharField(max_length=50)
    reporting_subjects = models.CharField(max_length=100)
    reporting_Notice = models.TextField()

    def __str__(self):
        return self.reporting_name

