from rest_framework import serializers
from .models import Merch
from django.contrib.auth.models import User

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merch
        fields = '__all__' # dunder method returning all fields

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
    

