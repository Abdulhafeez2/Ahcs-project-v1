import json

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from accounts.models import Staff, User
from login import decorators, urls
from login.views import user_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='login_url')
# @decorators.nurseonly
from patient.forms import VitalSignForm
from patient.models import Patient
from receptionist.models import Triage


def nurse_homepage(request):
    try:
        triage_list = Triage.objects.filter(hospital_id=Staff.objects.get(basic_id=request.user.id).hospital_id,
                                            status='pending')
        triage = True
        context = {'triage': triage, 'triage_list': triage_list}
        return render(request, "nurse/homepage.html", context)
    except:
        triage = False
        context = {'triage': triage}
        return render(request, "nurse/homepage.html", context)


def add_vital_sign(request, pk):
    msg = 'successfully added'
    if request.method == 'POST':
        form = VitalSignForm(request.POST)
        patient = Patient.objects.get(basic_id=pk)
        staff = Staff.objects.get(basic_id=request.user.id)
        context = {'patient': patient, 'staff': staff}
        if form.is_valid():
            form.save_vital_sign(context)
            triage = Triage.objects.filter(patient_id=patient.id).first()
            triage.status = 'approved'
            triage.save()
            #nxt = request.POST.get('next', '/')
            return redirect('admit_to_dr_url')
        else:
            form = VitalSignForm
            patient = User.objects.get(id=pk)
            context = {'form': form, 'patient': patient}
            return render(request, "nurse/form/vital_sign_form.html", context)


    else:
        form = VitalSignForm

        patient = User.objects.get(id=pk)
        context = {'form': form, 'patient': patient}
        return render(request, "nurse/form/vital_sign_form.html", context)


def admit_to_dr(request, pk):

    form = VitalSignForm
    patient = User.objects.get(id=pk)
    context = {'form': form, 'patient': patient}
    return render(request, "nurse/form/admit_to_dr.html", context)

def find_available_physician(request,value):
    doc=User.objects.get(id=Staff.objects.get(specialty=value).basic_id).username
    return HttpResponse(doc)