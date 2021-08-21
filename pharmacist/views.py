from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from accounts.models import Pharmacy
from login.decorators import allowed_users


@login_required(login_url='login_url')
@allowed_users(allowed_roles=['pharmacist'])
def pharmacist_homepage(request):
    return render(request, 'pharmacist/homepage.html')

@allowed_users(allowed_roles=['pharmacist'])
@login_required(login_url='login_url')
def patient_detail(request):
    return render(request, 'pharmacist/form/patient_descriptions.html')