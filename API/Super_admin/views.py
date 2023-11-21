from django.shortcuts import render
from django.contrib.auth.models import Group
from rest_framework.response import Response
from .models import *
from rest_framework.decorators import api_view, permission_classes
from .serializers import *
from rest_framework.permissions import IsAuthenticated

group_f = Group.objects.get_or_create(name="Faculty")
group_p = Group.objects.get_or_create(name="Parents")
group_s = Group.objects.get_or_create(name="Student")


def home(request):
    return render(request, 'home.html')


@api_view(['POST'])
def register(request):
    serial = Userserializers(data=request.data)
    if serial.is_valid():
        serial.save()
        return Response(serial.data)
    else:
        content = {'status': 'not valid'}
        return Response(content)


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            log = User.objects.get(email=email)
            if password == log.password:
                request.session['email'] = email
                content = {'status': 'login'}
                return Response(content)
            else:
                content = {'status': 'Password Not match'}
                return Response(content)
        except:
            content = {'status': 'Email not match'}
            return Response(content)
    else:
        content = {'status': 'login again'}
        return Response(content)


@api_view(['GET'])
def logout(request):
    del request.session['email']
    content = {'status': 'Logout Successfully'}
    return Response(content)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_register(request):
    data = User.objects.all()
    serializer = Userserializers(data, many=True)
    return Response(serializer.data)


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def profile(request):
#     data = User.objects.get(email=request.session['email'])
#     if request.method == 'POST':
#         serial = Profileserializers(data=request.data)
#         if serial.is_valid():
#             serial.save()
#             return Response(serial.data)
#         else:
#             return Response(headers='not valid')
#     else:
#         return Response(headers='not edit profile')
