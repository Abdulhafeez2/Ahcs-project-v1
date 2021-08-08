from django.shortcuts import render
from login import urls
from django.contrib.auth.decorators import login_required
from login import decorators
# Create your views here.

#@login_required(login_url='login_url')
#@decorators.physicianonly
def physician_homepage(request):
    context = {}
    return render(request, 'physician/physician_dashboard.html')


@login_required(login_url='login_url')
@decorators.physicianonly
def view_waiting_list(request):
    context={ }
    return render(request,"physician/forms/view_waiting_list.html",context)

@login_required(login_url='login_url')
@decorators.physicianonly
def add_prescription(request):
    context={ }
    return render(request,"physician/forms/prescription_form.html",context)

@login_required(login_url='login_url')
@decorators.physicianonly
def add_xray_request(request):
    context={ }
    return render(request,"physician/forms/xray_form.html",context)