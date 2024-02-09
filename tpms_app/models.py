from django.db import models


class AdminDetails(models.Model):
    username = models.CharField(max_length = 200, blank = True , null = True)
    password = models.CharField(max_length = 200, blank = True , null = True)


class UserDetails(models.Model):
    profile = models.FileField(upload_to='profile', blank = True , null = True)
    email = models.CharField(max_length = 200, blank = True , null = True)
    phone = models.CharField(max_length = 200, blank = True , null = True)
    username = models.CharField(max_length = 200, blank = True , null = True)
    password = models.CharField(max_length = 200, blank = True , null = True)
    created_dt = models.DateTimeField(  blank = True , null = True )


