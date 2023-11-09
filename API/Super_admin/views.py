from django.shortcuts import render
from django.contrib.auth.models import Group
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from .models import *

group_f = Group.objects.get_or_create(name="Faculty")
group_p = Group.objects.get_or_create(name="Parents")
group_s = Group.objects.get_or_create(name="Student")


view_all_users_permission = Permission.objects.get(codename='add_register')
edit_all_users_permission = Permission.objects.get(codename='change_register')


def home(request):
    return render(request, 'home.html')

# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = Userserializers
