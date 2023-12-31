from django.db import models


class User(models.Model):
    SUPERADMIN = 1
    ADMIN = 2
    FACULTY = 3
    PARENTS = 4
    STUDENT = 5

    ROLE_CHOICE = (
        (SUPERADMIN, 'superadmin'),
        (ADMIN, 'admin'),
        (FACULTY, 'faculty'),
        (PARENTS, 'parents'),
        (STUDENT, 'student')
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role_choice = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, default=3)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Profile(models.Model):
    profile_name = models.CharField(max_length=500)
    profile_address = models.CharField(max_length=500)
    profile_gender = models.CharField(max_length=100)
    profile_M_number = models.IntegerField(default=0)
    profile_DOB = models.DateField()
    profile_status = models.CharField(max_length=200)

    def __str__(self):
        return self.profile_name


class Add_student(models.Model):
    student_name = models.CharField(max_length=500)
    student_address = models.TextField()
    student_course = models.CharField(max_length=500)
    student_DOB = models.DateField()

    def __str__(self):
        return self.student_name + " " + self.student_course


class Add_faculty(models.Model):
    faculty_name = models.CharField(max_length=500)
    faculty_position = models.CharField(max_length=200)
    faculty_address = models.CharField(max_length=500)
    faculty_exprience = models.CharField(max_length=200)
    faculty_subjects = models.CharField(max_length=200)
    faculty_class = models.CharField(max_length=300)

    def __str__(self):
        return self.faculty_name + " " + self.faculty_position


class Add_admin(models.Model):
    admin_name = models.CharField(max_length=500)
    admin_address = models.CharField(max_length=500)
    admin_DOB = models.DateField()
    admin_exprince = models.CharField(max_length=200)

    def __str__(self):
        return self.admin_name


class Add_parents(models.Model):
    parents_name = models.CharField(max_length=200)
    student_name = models.CharField(max_length=200)
    parents_address = models.TextField()
    parents_gender = models.CharField(max_length=20)

    def __str__(self):
        return self.parents_name + " " + self.student_name


class Add_event_activite(models.Model):
    E_A_name = models.CharField(max_length=300)
    E_A_Notice = models.TextField()

    def __str__(self):
        return self.E_A_name


class Fees_notice(models.Model):
    Student_name = models.CharField(max_length=100)
    fees_notice = models.TextField()

    def __str__(self):
        return self.Student_name


class Time_table(models.Model):
    school_std = models.CharField(max_length=30, null=True)
    school_start = models.TimeField(null=True)
    school_end = models.TimeField(null=True)
    school_day1 = models.CharField(max_length=20, null=True)
    day1_subject = models.TextField(null=True)
    school_day2 = models.CharField(max_length=20, null=True)
    day2_subject = models.TextField(null=True)
    school_day3 = models.CharField(max_length=20, null=True)
    day3_subject = models.TextField(null=True)
    school_day4 = models.CharField(max_length=20, null=True)
    day4_subject = models.TextField(null=True)
    school_day5 = models.CharField(max_length=20, null=True)
    day5_subject = models.TextField(null=True)
    school_day6 = models.CharField(max_length=20, null=True)
    day6_subject = models.TextField(null=True)

    def __str__(self):
        return self.school_std


class Exam_time_table(models.Model):
    exam_std = models.CharField(max_length=50)
    exam_date = models.CharField(max_length=200)
    exam_subject = models.CharField(max_length=200)
    exam_time = models.TimeField()

    def __str__(self):
        return self.exam_std
