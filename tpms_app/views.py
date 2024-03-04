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
    request_count = PasswordRequest.objects.filter(status = 'PENDING').count()
    toll_info = TollCollection.objects.all().count()
    today_toll_collect = TollCollection.objects.filter(created_dt__date = datetime.date.today()).count()
    emp_obj = UserDetails.objects.filter(status = 'Unblock').order_by('-id')[:5]
    total_visitor = VehicleMaster.objects.all().count()


    context = {'login_type': login_type  , 'user' : user , 'toll_info' : toll_info , 'emp_obj': emp_obj , 'today_toll_collect': today_toll_collect , 'total_visitor': total_visitor, 'request_count': request_count}
    return render(request, 'admin_panel/Dashboard.html', context)

@handle_page_exception
def employee(request, user , login_type):
    employee = UserDetails.objects.all().order_by('-id')
    request_count = PasswordRequest.objects.filter(status = 'PENDING').count()
    context = {'login_type': login_type  , 'user' : user ,'employee': employee, 'request_count': request_count}
    return render(request, 'admin_panel/employee.html', context)

@handle_page_exception
def request(request, user , login_type):
    request_obj = PasswordRequest.objects.filter(status = 'PENDING').order_by('-id')
    request_count = PasswordRequest.objects.filter(status = 'PENDING').count()
    context = {'login_type': login_type  , 'user' : user ,'request_obj': request_obj , 'request_count': request_count }
    return render(request, 'admin_panel/request.html', context)

@handle_page_exception
def new_employe(request, user , login_type):
    request_count = PasswordRequest.objects.filter(status = 'PENDING').count()
    context = {'login_type': login_type  , 'user' : user, 'request_count': request_count }
    return render(request, 'admin_panel/new_employe.html', context)
    

@handle_page_exception
def register_vehicle(request, user ,login_type  ):
    request_count = PasswordRequest.objects.filter(status = 'PENDING').count()
    context = {'login_type': login_type, 'user' : user, 'request_count': request_count}
    return render(request, 'user_panel/register_vehicle.html' , context)


@handle_page_exception
def setup_toll_info(request, user , login_type):
    toll_obj = TollInfo.objects.all().order_by('-id')
    request_count = PasswordRequest.objects.filter(status = 'PENDING').count()
    context = {'login_type': login_type , 'toll_obj' : toll_obj, 'user' : user, 'request_count': request_count}
    return render(request, 'admin_panel/setup_toll_info.html'  ,context)

@handle_page_exception
def toll_info(request, user , login_type):
    toll_obj = TollInfo.objects.all().order_by('-id')
    request_count = PasswordRequest.objects.filter(status = 'PENDING').count()
    context = {'login_type': login_type ,  'toll_obj' : toll_obj, 'user' : user, 'request_count': request_count}
    return render(request, 'user_panel/toll_info.html'  ,context)


@handle_page_exception
def manage_vehicle(request, user , login_type ):
    veh_obj = VehicleMaster.objects.all().order_by('-id')
    request_count = PasswordRequest.objects.filter(status = 'PENDING').count()
    rendered = render_to_string('user_panel/render_to_string/r_t_s_vehicles.html', {'veh_obj' : veh_obj})
    context = {'rendered' : rendered , 'login_type': login_type , 'user' : user, 'request_count': request_count}
    return render(request, 'user_panel/manage_vehicle.html', context)
    
@handle_page_exception
def toll_collection(request, user , login_type ):
    toll_obj = TollInfo.objects.all().order_by('-id')
    request_count = PasswordRequest.objects.filter(status = 'PENDING').count()
    context = {'toll_obj' : toll_obj , 'login_type': login_type , 'user' : user, 'request_count': request_count}
    return render(request, 'user_panel/toll_collection.html', context)
    
@handle_page_exception
def toll_collection_history(request, user , login_type ):
    toll_obj = TollCollection.objects.all().order_by('-id')
    request_count = PasswordRequest.objects.filter(status = 'PENDING').count()
    rendered = render_to_string('user_panel/render_to_string/r_t_s_toll_history.html', {'toll_obj' : toll_obj})
    context = {'rendered' : rendered , 'login_type': login_type , 'user' : user, 'request_count': request_count}
    return render(request, 'user_panel/toll_collection_history.html', context)


@handle_page_exception
def profile(request, user , login_type ):
    request_count = PasswordRequest.objects.filter(status = 'PENDING').count()
    context = {'user' : user , 'login_type': login_type , 'user' : user, 'request_count': request_count}
    return render(request, 'user_panel/profile.html', context)

@handle_page_exception
def modify_details(request, user , login_type , id ):
    veh_obj  = VehicleMaster.objects.get(id = id)
    request_count = PasswordRequest.objects.filter(status = 'PENDING').count()
    context = { 'veh_obj' : veh_obj , 'login_type': login_type, 'user' : user, 'request_count': request_count}
    return render(request, 'user_panel/register_vehicle.html', context)
    
@handle_page_exception
def EditEmp(request, user , login_type , id ):
    emp_obj  = UserDetails.objects.get(id = id)
    request_count = PasswordRequest.objects.filter(status = 'PENDING').count()
    context = { 'emp_obj' : emp_obj , 'login_type': login_type, 'user' : user, 'request_count': request_count}
    return render(request, 'admin_panel/new_employe.html', context)
    


# WEBSITE


def web_home(request):
    return render(request, 'website/index.html')