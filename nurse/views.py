from django.shortcuts import render
from login import decorators, urls
from login.views import user_logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login_url')
#@decorators.nurseonly
def nurse_homepage(request):
    context={}
    return render(request,"nurse/nurse_dashboard.html",context)
def add_vital_sign(request):
    context={}
    return render(request,"nurse/form/vital_sign_form.html",context)