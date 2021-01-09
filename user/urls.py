from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from . import views

router = DefaultRouter()
router.register('basicdetails', views.BasicDetailAPI, basename='basicdetails')
router.register('parmanentaddress', views.ParmanentAddressAPI, basename='parmanentaddress')
router.register('user', views.UserAPI, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('gettoken/', TokenObtainPairView.as_view(), name='get_token'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='refresh_token'),
    path('velidatetoken/', TokenVerifyView.as_view(), name='velidate_token'),
]