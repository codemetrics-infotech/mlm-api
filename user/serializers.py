from rest_framework import serializers
from .models import BasicDetail, ParmanentAddress

class BasicDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicDetail
        fields = '__all__'

class ParmanentAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParmanentAddress
        fields = '__all__'