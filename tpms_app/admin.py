from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(AdminDetails)
class AdminDetailsAdmin(admin.ModelAdmin):
    list_display = ('id' , 'username', 'password')


@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone', 'username' , 'password', 'created_dt' )