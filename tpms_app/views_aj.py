from django.http import JsonResponse
from Project_utilty.decorators import *
from .models import *
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def user_login_aj(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    send_data = None
    if UserDetails.objects.filter(username = username , password = password).exists():
        user_obj = UserDetails.objects.get(username = username , password = password)
        request.session['user_id'] = user_obj.id
        request.session['user_type'] = 'user'
        send_data = {'status': 1 , 'msg' : 'Successfully Login...' }
        type = 'user'
    elif AdminDetails.objects.filter(username = username , password = password).exists():
        user_obj = AdminDetails.objects.get(username = username , password = password)
        request.session['admin_user_id'] = user_obj.id
        request.session['admin_user_type'] = 'admin'
        type = 'admin'
        send_data = {'status': 1 , 'msg' : 'Admin Login Successfully...' , 'type':type}
    else:
        send_data = {'status': 0 , 'msg' : 'Invalid Credentials' }
    return JsonResponse(send_data)


def logout(request):
    try:
        del request.session['user_id']
        del request.session['user_type']
    except:
        del request.session['admin_user_id']
        del request.session['admin_user_type']
    return redirect('/')


@csrf_exempt
@handle_ajax_exception
def Save_Vehicle_Details(request):
    data = request.POST.dict()
    val_id = request.POST.get('val_id')
    data.pop('val_id')
    msg = 'Vehicle Registered'
    if val_id != "" and VehicleMaster.objects.filter(id = val_id).exists() :
        VehicleMaster.objects.filter(id = val_id).update(**data)
        msg = 'Vehicle Modified'
    else:
        VehicleMaster.objects.create(**data)
        msg = 'Vehicle Registered'
    send_data = {'status': 1 , 'msg' : msg }
    return JsonResponse(send_data)


@csrf_exempt
@handle_ajax_exception
def Add_Employee(request):
    data = request.POST.dict()
    val_id = request.POST.get('val_id')
    data.pop('val_id')
    print(data)
    if val_id != "" and UserDetails.objects.filter(id = val_id).exists() :
        UserDetails.objects.filter(id = val_id).update(**data)
        msg = 'Employee Details updated'
    else:
        obj = UserDetails.objects.create(**data)
        obj.status = 'Unblocked'
        obj.save()
        msg = 'Employee Added'
    send_data = {'status': 1 , 'msg' : msg }
    return JsonResponse(send_data)



@csrf_exempt
@handle_ajax_exception
def Save_Toll_info(request):
    data = request.POST.dict()
    val_id = request.POST.get('val_id')
    data.pop('val_id')
    msg = 'Vehicle Registered Successfully'

    if val_id != "" and TollInfo.objects.filter(id = val_id).exists() :
        TollInfo.objects.filter(id = val_id).update(**data)
        msg = 'Vehicle Modified Successfully'
    else:
        TollInfo.objects.create(**data)
        msg = 'Vehicle Registered Successfully'
    send_data = {'status': 1 , 'msg' :msg }
    return JsonResponse(send_data)
    
@csrf_exempt
@handle_ajax_exception
def Delete_Record(request):
    id = request.POST.get("id")
    VehicleMaster.objects.filter(id = id).delete()
    return JsonResponse({'status':1, 'msg': "Recored Removed"})


@csrf_exempt
@handle_ajax_exception
def Delete_Employee(request):
    id = request.POST.get("id")
    UserDetails.objects.filter(id = id).delete()
    return JsonResponse({'status':1, 'msg': "Recored Removed"})


@csrf_exempt
@handle_ajax_exception
def Delete_Toll_Record(request):
    id = request.POST.get("id")
    TollInfo.objects.filter(id = id).delete()
    return JsonResponse({'status':1, 'msg': "Toll Record Deleted Successfully"})

@csrf_exempt
@handle_ajax_exception
def Delete_Toll_Collected_Record(request):
    id = request.POST.get("id")
    TollCollection.objects.filter(id = id).delete()
    return JsonResponse({'status':1, 'msg': "Collected Toll Record Removed"})


@csrf_exempt
@handle_ajax_exception
def Get_Tax_Amout(request):
    value = request.POST.get('value')
    amt = 0
    if (value != ""):
        obj = TollInfo.objects.get(id = value)
        amt = obj.toll_amt
    return JsonResponse({'status': 1, 'response_amount' : amt})

@csrf_exempt
@handle_ajax_exception
def CashCollected(request):
    data = request.POST.dict()
    TollCollection.objects.create(**data)
    return JsonResponse({'status':1 , 'msg' : 'Toll Collected.'})


@csrf_exempt
@handle_ajax_exception
def Save_Profile_Changes(request):
    data = request.POST.dict()
    user_id = request.POST.get('user_id')
    user = request.POST.get('user')
    profile = request.FILES.get('profile')
    data.pop('user_id')
    print(data)
    if 'profile' in data:
        data.pop('profile')
    data.pop('user')
    if user == 'user' and UserDetails.objects.filter(id = user_id).exists():
        UserDetails.objects.filter(id = user_id).update(**data)
        user_obj = UserDetails.objects.get(id = user_id)
        user_obj.profile = profile if profile else user_obj.profile
        user_obj.save()
        send_data = {'status':1 , 'msg' : 'Data Updated.'}
    else:
        send_data = {'status':0 , 'msg' : 'Something went wrong.'}
    return JsonResponse(send_data)


@csrf_exempt
@handle_ajax_exception
def SendRequest(request):
    user_id = request.POST.get('user_id')
    request_txt = request.POST.get('request_txt')
    PasswordRequest.objects.create(fk_user_id = user_id , reason = request_txt , status = 'PENDING')
    return JsonResponse({'status':1, 'msg': 'Password Request Send Successfully...'})

@csrf_exempt
@handle_ajax_exception
def Block_Employee(request):
    user_id = request.POST.get('user_id')
    type = request.POST.get('type')
    UserDetails.objects.filter(id = user_id ).update(status = type)
    return JsonResponse({'status':1, 'msg': 'Employee Data Changed Successfully...'})


@csrf_exempt
@handle_ajax_exception
def Change_Employee(request):
    user_id = request.POST.get('user_id')
    password = request.POST.get('password')
    UserDetails.objects.filter(id = user_id ).update(password = password)
    PasswordRequest.objects.filter(fk_user_id = user_id).update(status = 'COMPLETED')
    return JsonResponse({'status':1, 'msg': 'Password Changed Successfully...'})