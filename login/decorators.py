from django.http import HttpResponse
from django.shortcuts import redirect
from login import urls


def unauthenticated_user(view_func):
    def wrapper_func(request, *args,**kwargs):
        return view_func(request, *args,**kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def  decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            
            group = None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponse('You are not authorized to view this page!')
        return wrapper_func
    return decorator

def receptionistonly(view_func):
    def wrapper_function(request,*args,**kwargs):
        group=None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name
        if group =='Physician':
            return redirect('physician_homepage_url')
        if group =='Hospital_admin':
            return redirect('hospital_admin_homepage_url')
        
        if group =='Receptionist':
            return  view_func(request,*args,**kwargs)
    return wrapper_function

def hospital_adminonly(view_func):
    def wrapper_function(request,*args,**kwargs):
        group=None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name
        if group =='Receptionist':
            return redirect('receptionist_dashboard')
        if group =='Nurse':
            return redirect('nurse_dashboard')
        if group =='Physician':
            return redirect('physician_homepage_url')
        if group =='Hospital_admin':
            return  view_func(request,*args,**kwargs)
    return wrapper_function
    
        
def physicianonly(view_func):
    def wrapper_function(request,*args,**kwargs):
        group=None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name
        if group =='Receptionist':
            return redirect('receptionist_dashboard')
        if group =='Nurse':
            return redirect('nurse_dashboard')
        if group =='Hospital_admin':
            return redirect('hospital_admin_homepage_url')
        if group =='Physician':
            return  view_func(request,*args,**kwargs)
    return wrapper_function

        
def nurseonly(view_func):
    def wrapper_function(request,*args,**kwargs):
        group=None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name
        if group =='Receptionist':
            return redirect('receptionist_dashboard')
        if group =='Hospital_admin':
            return redirect('hospital_admin_homepage_url')
        if group =='Physician':
            return redirect('physician_homepage_url')
        if group =='Nurse':
            return  view_func(request,*args,**kwargs)
    return wrapper_function
        