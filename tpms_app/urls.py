from django.contrib import admin
from django.urls import path 
from .views import *
from .views_aj import *
from django.conf import settings
from django.conf.urls.static import static

admin_url = [
    path('user_login/', user_login ), 
    path('dashboard/', dashboard ),
    path('index/', index ),
]


ajax_url = [
    path('UserLogin/', user_login_aj)
]


website_url = [

]



urlpatterns = [*admin_url , *ajax_url , *website_url] + static( settings.MEDIA_URL , document_root = settings.MEDIA_ROOT  ) 