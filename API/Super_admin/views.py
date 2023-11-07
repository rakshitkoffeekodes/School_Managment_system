from django.shortcuts import render
from Super_admin.models import *
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Super_admin.serializers import Super_admin_registerserializers
from Super_admin.serializers import Super_admin_loginserializers


# Create your views here.

def home(request):
    return render(request, 'home.html')


@api_view(['GET'])
def register(request, fname, lname, email, password):
    Suprt_admin_register.objects.create(
        first_name=fname,
        last_name=lname,
        email=email,
        password=password
    )
    only = Suprt_admin_register.objects.all()
    serial = Super_admin_registerserializers(only, many=True)
    return Response(serial.data)


@api_view(['GET'])
def login(request, first, second):
    try:
        one = Suprt_admin_register.objects.get(email=first)
        try:
            two = Suprt_admin_register.objects.get(password=second)
            Super_admin_login.objects.create(
                login_email=first,
                login_password=second,
                login_datetime = datetime.now()
            )
            three = Super_admin_login.objects.all()
            serial = Super_admin_loginserializers(three, many=True)
            return Response(serial.data)
        except:
            return render(request, 'home.html', {"msg": "Password is Invalid"})
    except:
        return render(request, 'home.html', {"msg": "Email is Invalid"})


@api_view(['GET'])
def profile(request, pk, pname, padd, pgender, pmnumber, pdob, pstatus):
    try:
        one=Suprt_admin_register.objects.get(id=pk)
        one.profile_name = pname
        one.profile_address = padd
        one.profile_gender = pgender
        one.profile_M_number = pmnumber
        one.profile_DOB = pdob
        one.profile_status = pstatus
    except:
        pass
