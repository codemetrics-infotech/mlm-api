from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from .filters import UserFilterBackend, UserFilter
from .throttling import DetailsRateThrottle, AddressRateThrottle, UserRateThrottle
from .models import BasicDetail, ParmanentAddress
from .serializers import BasicDetailsSerializer, ParmanentAddressSerializer, UserSerializer

# Create your views here.

class BasicDetailAPI(viewsets.ModelViewSet):
    queryset = BasicDetail.objects.all()
    serializer_class = BasicDetailsSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [DetailsRateThrottle]
    filter_backends = [UserFilterBackend]
    filterset_class = UserFilter
    filterset_fields = ('username')
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    def get_filterset_kwargs(self):
        return {
            'username': self.get_username(),
        }

class ParmanentAddressAPI(viewsets.ModelViewSet):
    queryset = ParmanentAddress.objects.all()
    serializer_class = ParmanentAddressSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [AddressRateThrottle]
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]

# @method_decorator(csrf_exempt, name='despatch')
class UserAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    filter_backends = [UserFilterBackend]
    filterset_class = UserFilter
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]

class UserListAPI(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filetrset_filds = ['username']