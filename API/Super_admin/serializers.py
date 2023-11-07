from Super_admin.models import *
from rest_framework import serializers


class Super_admin_registerserializers(serializers.ModelSerializer):
    class Meta:
        model = Suprt_admin_register
        fields = '__all__'


class Super_admin_loginserializers(serializers.ModelSerializer):
    class Meta:
        model = Super_admin_login
        fields = '__all__'
