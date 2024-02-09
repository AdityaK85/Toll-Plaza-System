from django.http import JsonResponse
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
    else:
        send_data = {'status': 0 , 'msg' : 'Invalid Credentials' }
    return JsonResponse(send_data)