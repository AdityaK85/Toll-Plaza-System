from django.db import models
import datetime

class AdminDetails(models.Model):
    username = models.CharField(max_length = 200, blank = True , null = True)
    password = models.CharField(max_length = 200, blank = True , null = True)


class UserDetails(models.Model):
    profile = models.FileField(upload_to='profile', blank = True , null = True)
    email = models.CharField(max_length = 200, blank = True , null = True)
    phone = models.CharField(max_length = 200, blank = True , null = True)
    discription = models.TextField(blank = True , null = True)
    username = models.CharField(max_length = 200, blank = True , null = True)
    password = models.CharField(max_length = 200, blank = True , null = True)
    salary = models.CharField(max_length = 200, blank = True , null = True)
    created_dt = models.DateTimeField( default = datetime.datetime.now(),   blank = True , null = True )


class VehicleMaster(models.Model):
    vehicle_no = models.CharField(max_length = 200, blank = True , null = True)
    vehicle_type = models.CharField(max_length = 200, blank = True , null = True)
    owner_info = models.CharField(max_length = 200, blank = True , null = True)
    registration_no = models.CharField(max_length = 200, blank = True , null = True)
    vehicle_color = models.CharField(max_length = 200, blank = True , null = True)
    payment_pefernce = models.CharField(max_length = 200, blank = True , null = True)
    insurance = models.CharField(max_length = 200, blank = True , null = True)
    created_dt = models.DateTimeField( default = datetime.datetime.now(),   blank = True , null = True )
     


#  Toll Information set only Admin
class TollInfo(models.Model):
    vehicle_type = models.CharField(max_length = 200, blank = True , null = True)
    toll_amt = models.FloatField(blank = True , null = True)
    valid_toll_hr = models.CharField(max_length = 200, blank = True , null = True)  # Toll Valid for 24 Hours



class TollCollection(models.Model):
    vehicle_identification = models.CharField(max_length = 200, blank = True , null = True)
    vehicle_type = models.CharField(max_length = 200, blank = True , null = True)
    veh_no = models.CharField(max_length = 200, blank = True , null = True)
    state = models.CharField(max_length = 200, blank = True , null = True)
    addr = models.CharField(max_length = 200, blank = True , null = True)
    lane_code = models.CharField(max_length = 200, blank = True , null = True)
    fee_sehedule = models.CharField(max_length = 200, blank = True , null = True)
    payment_by = models.CharField(max_length = 200, blank = True , null = True)
    payment_recipt = models.FileField(upload_to='payment_recipt', blank = True , null = True)
    lane_code = models.CharField(max_length = 200, blank = True , null = True)