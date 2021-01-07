from django.shortcuts import render
from rest_framework import viewsets
from .models import BasicDetail, ParmanentAddress
from .serializers import BasicDetailsSerializer, ParmanentAddressSerializer

# Create your views here.

class BasicDetailAPI(viewsets.ModelViewSet):
    queryset = BasicDetail.objects.all()
    serializer_class = BasicDetailsSerializer

class ParmanentAddressAPI(viewsets.ModelViewSet):
    queryset = ParmanentAddress.objects.all()
    serializer_class = ParmanentAddressSerializer