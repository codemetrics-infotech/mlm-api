from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import DjangoModelPermissions
from .models import BasicDetail, ParmanentAddress
from .serializers import BasicDetailsSerializer, ParmanentAddressSerializer, UserSerializer

# Create your views here.

class BasicDetailAPI(viewsets.ModelViewSet):
    queryset = BasicDetail.objects.all()
    serializer_class = BasicDetailsSerializer

class ParmanentAddressAPI(viewsets.ModelViewSet):
    queryset = ParmanentAddress.objects.all()
    serializer_class = ParmanentAddressSerializer

# @method_decorator(csrf_exempt, name='despatch')
class UserAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions]