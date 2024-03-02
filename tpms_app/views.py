from django.shortcuts import render
from Project_utilty.decorators import *
from .models import *
from django.template.loader import render_to_string

def index(request):
    return render(request, 'user_panel/index.html')


def user_login(request):
    return render(request, 'user_panel/login.html')
    

@handle_page_exception
def dashboard(request, user , login_type):
    context = {'login_type': login_type}
    return render(request, 'user_panel/dashboard.html', context)
    

@handle_page_exception
def register_vehicle(request, user ,login_type  ):
    context = {'login_type': login_type}
    return render(request, 'user_panel/register_vehicle.html' , context)


@handle_page_exception
def setup_toll_info(request, user , login_type):
    toll_obj = TollInfo.objects.all().order_by('-id')
    context = {'login_type': login_type , 'toll_obj' : toll_obj}
    return render(request, 'admin_panel/setup_toll_info.html'  ,context)

@handle_page_exception
def toll_info(request, user , login_type):
    toll_obj = TollInfo.objects.all().order_by('-id')
    context = {'login_type': login_type ,  'toll_obj' : toll_obj}
    return render(request, 'user_panel/toll_info.html'  ,context)


@handle_page_exception
def manage_vehicle(request, user , login_type ):
    veh_obj = VehicleMaster.objects.all().order_by('-id')
    rendered = render_to_string('user_panel/render_to_string/r_t_s_vehicles.html', {'veh_obj' : veh_obj})
    context = {'rendered' : rendered , 'login_type': login_type }
    return render(request, 'user_panel/manage_vehicle.html', context)
    
@handle_page_exception
def toll_collection(request, user , login_type ):
    toll_obj = TollInfo.objects.all().order_by('-id')
    context = {'toll_obj' : toll_obj , 'login_type': login_type }
    return render(request, 'user_panel/toll_collection.html', context)
    
@handle_page_exception
def toll_collection_history(request, user , login_type ):
    toll_obj = TollCollection.objects.all().order_by('-id')
    rendered = render_to_string('user_panel/render_to_string/r_t_s_toll_history.html', {'toll_obj' : toll_obj})
    context = {'rendered' : rendered , 'login_type': login_type }
    return render(request, 'user_panel/toll_collection_history.html', context)


@handle_page_exception
def profile(request, user , login_type ):
    context = {'user' : user , 'login_type': login_type }
    return render(request, 'user_panel/profile.html', context)

@handle_page_exception
def modify_details(request, user , login_type , id ):
    veh_obj  = VehicleMaster.objects.get(id = id)
    context = { 'veh_obj' : veh_obj , 'login_type': login_type}
    return render(request, 'user_panel/register_vehicle.html', context)
    