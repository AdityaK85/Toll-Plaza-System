from django.contrib import admin
from django.urls import path 
from .views import *
from .views_aj import *
from django.conf import settings
from django.conf.urls.static import static

admin_url = [
    path('user_login/', user_login ), 
    path('web_home/', web_home ), 
    path('Dashboard/', dashboard ),
    path('employee/', employee ),
    path('new_employe/', new_employe ),
    path('register_vehicle/', register_vehicle ),
    path('manage_vehicle/', manage_vehicle ),
    path('setup_toll_info/', setup_toll_info ),
    path('toll_info/', toll_info ),
    path('toll_collection/', toll_collection ),
    path('modify_details/<int:id>', modify_details ),
    path('toll_collection_history/', toll_collection_history ),
    path('profile/', profile ),
    path('index/', index ),
    path('request/', request ),
    path('EditEmp/<int:id>', EditEmp),
]


ajax_url = [
    path('UserLogin/', user_login_aj),
    path('logout/', logout),
    path('Save_Vehicle_Details/', Save_Vehicle_Details),
    path('Save_Toll_info/', Save_Toll_info),
    path('Delete_Record/', Delete_Record),
    path('Delete_Toll_Record/', Delete_Toll_Record),
    path('Get_Tax_Amout/', Get_Tax_Amout),
    path('Block_Employee/', Block_Employee),
    path('CashCollected/', CashCollected),
    path('Delete_Toll_Collected_Record/', Delete_Toll_Collected_Record),
    path('Save_Profile_Changes/', Save_Profile_Changes),
    path('SendRequest/', SendRequest),
    path('Add_Employee/', Add_Employee),
    path('Delete_Employee/', Delete_Employee),
    path('Change_Employee/', Change_Employee),
    
]


website_url = [

]



urlpatterns = [*admin_url , *ajax_url , *website_url] + static( settings.MEDIA_URL , document_root = settings.MEDIA_ROOT  ) 