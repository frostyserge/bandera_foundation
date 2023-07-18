from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Merch)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

class AppUserAdmin(admin.ModelAdmin):
    list_editable = ['verified']
    list_display = ['username', 'email']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'wallet', 'verified']