import traceback
from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from tpms_app.models import *
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from functools import wraps


def is_admin_authenticated(request):
    try:
		
        user_type = request.session.get('admin_user_type')
        user_id = request.session.get('admin_user_id')
		
        if user_type and user_id:
            if user_type == 'admin':
                user = AdminDetails.objects.get(id=user_id)
            else:
                user = AdminDetails.objects.get(id=user_id)
            return user
        else:
            return None
    except:
        traceback.print_exc()
    return None



### check request is authenticated or not 
def is_authenticated(request):
	try:
		user_type = request.session.get('user_type')
		user_id = request.session.get('user_id')

		if user_type and user_id:
			if user_type == 'user':
				user = UserDetails.objects.get(id=user_id)
			else:
				user = AdminDetails.objects.get(id=user_id)
			return user
		else:
			return None
	except:
		traceback.print_exc()
		return None




def handle_admin_page_exception(func):
	'''Function template to handle POST request and handle exceptions...'''
	def wrapper(request, *args, **kwargs):
		try:
			user = is_admin_authenticated(request)
			if user:
				return func(request, user, *args, **kwargs)
			else:
				return redirect('/')
		except:
			traceback.print_exc()
		return render(request, 'htmls/error_page.html')
		# return HttpResponse('Something went wrong')
	return wrapper

def handle_page_exception(func):
	'''Function template to handle POST request and handle exceptions...'''
	def wrapper(request, *args, **kwargs):
		try:
			user = is_authenticated(request)
			# Add New this lines 
			if user:
				login_type = request.session['user_type']   # New 
				return func(request, user, login_type,  *args, **kwargs)
			
			elif is_admin_authenticated(request):
				
				login_type = request.session['admin_user_type']    # New Line
				user = is_admin_authenticated(request)

				return func(request, user, login_type ,  *args, **kwargs)
			else:
				return redirect('/user_login')
		except:
			traceback.print_exc()
		return HttpResponse('Something went wrong')
	return wrapper

def handle_ajax_exception(func):
	'''Function template to handle POST request and handle exceptions...'''
	def wrapper(request, *args, **kwargs):
		send_data = {'status': 0, 'msg': 'Something went wrong.'}
		try:
			if request.method == 'POST':
				return func(request, *args, **kwargs)
			else:
				send_data['msg'] = 'POST method required.'
		except ObjectDoesNotExist:
			send_data['msg'] = 'Object not found.'
		except:
			traceback.print_exc()
		return JsonResponse(send_data)
	return wrapper


def get_date_label(posted_date, todays_date):
	yesterday = todays_date - timedelta(days=1)
	if posted_date != "" and posted_date != None:
		if todays_date == posted_date.date():
			return "Today"
		elif yesterday == posted_date.date():
			return "Yesterday"
		else:
			return posted_date.date().strftime("%d-%m-%Y")
	

