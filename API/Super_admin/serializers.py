from Super_admin.models import *
from rest_framework import serializers


class Userserializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'role_choice', 'password')


class Profileserializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'profile_name', 'profile_address', 'profile_gender', 'profile_M_number', 'profile_DOB', 'profile_status')
