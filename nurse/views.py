import json
from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from accounts.models import Staff, User, Hospital
from login import decorators, urls
from login.views import user_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='login_url')
# @decorators.nurseonly
from patient.forms import VitalSignForm
from patient.models import Patient
from physician.models import PatientWaitingList
from receptionist.models import Triage


def nurse_homepage(request):
    try:
        triage_list = Triage.objects.filter(hospital_id=Staff.objects.get(basic_id=request.user.id).hospital_id,
                                            status='pending')
        triage = True
        context = {'triage': triage, 'triage_list': triage_list}
        return render(request, "nurse/patient_detail.html", context)
    except:
        triage = False
        context = {'triage': triage}
        return render(request, "nurse/patient_detail.html", context)


def add_vital_sign(request, pk):
    msg = 'successfully added'
    if request.method == 'POST':
        form = VitalSignForm(request.POST)
        patient = Patient.objects.get(basic_id=pk)
        staff = Staff.objects.get(basic_id=request.user.id)
        context = {'patient': patient, 'staff': staff}
        if form.is_valid():
            form.save_vital_sign(context)
            # nxt = request.POST.get('next', '/')
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
    distinct = Staff.objects.filter(hospital_id=Staff.objects.get(basic_id=request.user.id).
                                    hospital_id).values('specialty').exclude(specialty=None).distinct()

    form = VitalSignForm
    patient = User.objects.get(id=pk)
    context = {'form': form, 'patient': patient, 'distinct': distinct}
    return render(request, "nurse/form/admit_to_dr.html", context)


def find_available_physician(request, value):
    doc = User.objects.get(id=Staff.objects.filter(specialty=value).first().basic_id)
    return HttpResponse(doc)


def assign_doctor(request):
    doctor = request.POST['doctor']
    patient = request.POST['patient']
    waiting_list = PatientWaitingList.objects.create(
        hospital_id=Hospital.objects.get(id=Staff.objects.get(basic_id=request.user.id).hospital_id).id,
        physician_id=Staff.objects.get(basic_id=User.objects.get(username=doctor)).id,
        patient_id=Patient.objects.get(basic_id=User.objects.get(id=patient)).id,
        added_by_id=Staff.objects.get(basic_id=request.user.id).id,
        status='pending',
    )
    waiting_list.save()
    triage = Triage.objects.filter(patient_id=Patient.objects.get(basic_id=patient)).first()
    triage.status = 'approved'
    triage.save()
    return redirect('nurse_homepage_url')
