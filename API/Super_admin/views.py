from django.shortcuts import render
from django.contrib.auth.models import Group
from rest_framework.response import Response
from .models import *
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from .serializers import Registerserializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAdminUser

group_f = Group.objects.get_or_create(name="Faculty")
group_p = Group.objects.get_or_create(name="Parents")
group_s = Group.objects.get_or_create(name="Student")


def home(request):
    return render(request, 'home.html')


@api_view(['GET'])
# @authentication_classes([BasicAuthentication])
# @permission_classes(['Can add user'])
def Register(request, fn, ln, em, ps):
    register.objects.create(
        first_name=fn,
        last_name=ln,
        email=em,
        password=ps
    )
    data = register.objects.all()
    serial = Registerserializers(data, many=True)
    return Response(serial.data)


@api_view(['GET'])
def Login(request, em, ps):
    if request.method == 'GET':
        try:
            log = register.objects.get(email=em)
            if ps == log.password:
                request.session['email'] = em
                contant = {'status': 'login'}
                return Response(contant)
            else:
                contant = {'status': 'password not match'}
                return Response(contant)
        except:
            contant = {'status': 'email not match'}
            return Response(contant)
    else:
        contant = {'status': 'login again'}
        return Response(contant)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_register(request):
    data = register.objects.all()
    serializer = Registerserializers(data, many=True)
    return Response(serializer.data)

