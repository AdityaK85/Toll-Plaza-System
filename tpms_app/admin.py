from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(AdminDetails)
class AdminDetailsAdmin(admin.ModelAdmin):
    list_display = ('id' , 'username', 'password')


@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone', 'username' , 'password', 'created_dt' )

@admin.register(VehicleMaster)
class VehicleMasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'vehicle_no', 'vehicle_type', 'owner_info' , 'registration_no', 'vehicle_color' , 'payment_pefernce' , 'insurance' , 'created_dt' )


@admin.register(TollInfo)
class TollInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'vehicle_type', 'toll_amt', 'valid_toll_hr' )

@admin.register(TollCollection)
class TollCollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'vehicle_identification', 'vehicle_type', 'fee_sehedule' , 'payment_by' , 'lane_code' )