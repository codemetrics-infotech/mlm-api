from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('basicdetails', views.BasicDetailAPI, basename='basicdetails')
router.register('parmanentaddress', views.ParmanentAddressAPI, basename='parmanentaddress')
router.register('user', views.UserAPI, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls'))
]