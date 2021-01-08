from rest_framework import serializers
from django.contrib.auth.models import User
from .models import BasicDetail, ParmanentAddress

class BasicDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicDetail
        fields = '__all__'

class ParmanentAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParmanentAddress
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'