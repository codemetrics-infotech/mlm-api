from django.contrib import admin
from .models import BasicDetail, ParmanentAddress

# Register your models here.

@admin.register(BasicDetail)
class BasicDetailAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'first_name', 'date_of_birth', 'email', 'mobile_number']

@admin.register(ParmanentAddress)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['address_id', 'user_id', 'city', 'state', 'nationality']