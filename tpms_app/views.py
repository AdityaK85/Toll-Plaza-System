from django.shortcuts import render


def index(request):
    return render(request, 'user_panel/index.html')


def user_login(request):
    return render(request, 'user_panel/login.html')
    
def dashboard(request):
    return render(request, 'user_panel/dashboard.html')
    