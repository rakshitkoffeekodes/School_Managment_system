from Super_admin.models import *
from rest_framework import serializers


#
#
# class Userserializers(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'role', 'password']
#
class Registerserializers(serializers.ModelSerializer):
    class Meta:
        model = register
        fields = '__all__'
