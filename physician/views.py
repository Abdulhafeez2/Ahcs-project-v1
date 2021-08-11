from django.shortcuts import render

from accounts.models import Staff
from login import urls
from django.contrib.auth.decorators import login_required
from login import decorators
# Create your views here.

#@login_required(login_url='login_url')
#@decorators.physicianonly
from patient.models import Patient
from physician.models import PatientWaitingList


def physician_homepage(request):
    try:
        patient_waiting_list = PatientWaitingList.objects.filter(physician_id=Staff.objects.get(basic_id=request.user.id).id,
                                                                 status='pending')
        waiting_list = True
        context = {'patient_waiting_list': patient_waiting_list, 'waiting_list': waiting_list}
        return render(request, "physician/physician_dashboard.html", context)
    except:
        waiting_list = False
        context = {'waiting_list': waiting_list}
        return render(request, "physician/physician_dashboard.html", context)


#@login_required(login_url='login_url')
#@decorators.physicianonly
def view_waiting_list(request):
    context = { }
    return render(request, "physician/forms/view_waiting_list.html", context)

@login_required(login_url='login_url')
@decorators.physicianonly
def add_prescription(request):
    context={ }
    return render(request,"physician/forms/prescription_form.html",context)

@login_required(login_url='login_url')

def add_radiology_request(request):
    context={ }
    return render(request,"physician/forms/xray_form.html",context)


def patient_detail(request, pk):
    waiting_list = PatientWaitingList.objects.filter(patient_id=pk).first()
    waiting_list.status = 'approved'
    waiting_list.save()
    user_profile = Patient.objects.get(id=pk)
    context = {'patient': pk, 'user_profile': user_profile}
    return render(request, "physician/patient_detail.html", context)


def lab_request(request):
    context = {}
    return render(request, "physician/forms/lab_request_form.html", context)