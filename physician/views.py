import datetime
from time import timezone

from django import forms
from django.shortcuts import render, redirect

from accounts.models import Staff, User, Hospital
from login import urls
from django.contrib.auth.decorators import login_required
from login import decorators
# Create your views here.

# @login_required(login_url='login_url')
# @decorators.physicianonly
from patient.models import Patient, VitalSign, PatientForm
from physician.forms import AddPatientForm, ReferralRequestForm, PrescriptionForm, AdministeredTreatmentForm, \
    XrayRequestForm, UltrasoundRequestForm
from physician.models import PatientWaitingList, Referral


def physician_homepage(request):
    try:
        patient_waiting_list = PatientWaitingList.objects.filter(
            physician_id=Staff.objects.get(basic_id=request.user.id).id,
            status='pending')
        waiting_list = True
        context = {'patient_waiting_list': patient_waiting_list, 'waiting_list': waiting_list}
        return render(request, "physician/physician_dashboard.html", context)
    except:
        waiting_list = False
        context = {'waiting_list': waiting_list}
        return render(request, "physician/physician_dashboard.html", context)


# @login_required(login_url='login_url')
# @decorators.physicianonly
def view_waiting_list(request):
    context = {}
    return render(request, "physician/forms/view_waiting_list.html", context)


@login_required(login_url='login_url')
@decorators.physicianonly
def add_prescription(request):
    context = {}
    return render(request, "physician/forms/prescription_form.html", context)


# @login_required(login_url='login_url')
def radiology_requests(request, pk):
    hospital_id = Staff.objects.get(basic_id=request.user.id).hospital.id
    xray_form = XrayRequestForm
    ultrasound_form = UltrasoundRequestForm
    context = {'xray_form': xray_form, 'ultrasound_form': ultrasound_form, 'pk': pk}
    return render(request, "physician/forms/xray_form.html", context)


def remove_from_list(request, pk):
    waiting_list = PatientWaitingList.objects.get(patient_id=pk, status='pending')
    waiting_list.status = 'approved'
    waiting_list.approval_time = datetime.datetime.now()
    waiting_list.save()
    staff = Staff.objects.get(basic_id=request.user.id)
    staff.num_waiting = staff.num_waiting - 1
    staff.save()
    return redirect('physician_homepage_url')


def patient_detail(request, pk):
    user_profile = Patient.objects.get(id=pk)
    try:
        latest_patient_form = PatientForm.objects.filter(patient_id=pk).latest('date')
    except:
        latest_patient_form = None
    try:
        vital_sign = VitalSign.objects.filter(patient_id=pk).latest('taken_date')
    except:
        vital_sign = None
    try:
        referral = Referral.objects.get(patient_id=pk, status='pending')
        print(referral)
    except:
        print("no referral")
        referral = None
    patient_form = AddPatientForm
    prescription_form = PrescriptionForm

    hospital_id = Staff.objects.get(basic_id=request.user.id).hospital.id
    referral_request = ReferralRequestForm(pk=hospital_id)

    administered_treatment = AdministeredTreatmentForm
    context = {'patient': pk, 'user_profile': user_profile, 'vital_sign': vital_sign,
               'patient_form': patient_form, 'prescription_form': prescription_form,
               'referral': referral, 'referral_request': referral_request,
               'latest_patient_form': latest_patient_form, 'administered_treatment': administered_treatment}
    return render(request, "physician/patient_detail.html", context)




def lab_request(request):
    context = {}
    return render(request, "physician/forms/lab_request_form.html", context)


def add_patient_form(request, pk):
    if request.method == 'POST':
        patient_form = AddPatientForm(request.POST)
        patient = Patient.objects.get(id=pk)
        staff = Staff.objects.get(basic_id=request.user.id)
        hospital = staff.hospital
        context = {'patient': patient, 'staff': staff, 'hospital': hospital}
        if patient_form.is_valid():
            patient_form.save_patient_form(context)
            # nxt = request.POST.get('next', '/')
            return redirect('patient_detail_url', pk)
        else:
            patient_form = AddPatientForm(request.POST)
            patient = User.objects.get(id=pk)
            context = {'patient_form': patient_form, 'patient': patient}
            return render(request, "nurse/form/vital_sign_form.html", context)


def add_referral(request, pk):
    if request.method == 'POST':
        referral_form = ReferralRequestForm(request.POST)
        patient = Patient.objects.get(id=pk)
        staff = Staff.objects.get(basic_id=request.user.id)
        hospital = staff.hospital
        context = {'patient': patient, 'staff': staff, 'hospital': hospital}
        if referral_form.is_valid():
            referral_form.save_referral(context)
            # nxt = request.POST.get('next', '/')
            return redirect('patient_detail_url', pk)
        else:
            print(referral_form.errors)


def add_prescription(request, pk):
    if request.method == 'POST':
        prescription_form = PrescriptionForm(request.POST)
        patient = Patient.objects.get(id=pk)
        staff = Staff.objects.get(basic_id=request.user.id)
        hospital = staff.hospital
        context = {'patient': patient, 'staff': staff, 'hospital': hospital}
        if prescription_form.is_valid():
            prescription_form.save_prescription(context)
            # nxt = request.POST.get('next', '/')
            return redirect('patient_detail_url', pk)


def administered_treatment(request, pk):
    if request.method == 'POST':
        administered_treatment_form = AdministeredTreatmentForm(request.POST)
        patient = Patient.objects.get(id=pk)
        staff = Staff.objects.get(basic_id=request.user.id)
        hospital = staff.hospital
        context = {'patient': patient, 'staff': staff, 'hospital': hospital}
        if administered_treatment_form.is_valid():
            administered_treatment_form.save_administered_treatment(context)
            # nxt = request.POST.get('next', '/')
            return redirect('patient_detail_url', pk)


def add_xray_request(request, pk):
    if request.method == 'POST':
        xray_form = XrayRequestForm(request.POST)
        print(xray_form.is_valid())
        patient = Patient.objects.get(id=pk)
        staff = Staff.objects.get(basic_id=request.user.id)
        hospital = staff.hospital
        context = {'patient': patient, 'staff': staff, 'hospital': hospital}
        if xray_form.is_valid():
            xray_form.save_xray_request(context)
            # nxt = request.POST.get('next', '/')
            return redirect('radiology_request_url', pk)
        else:
            print(xray_form.errors)


def add_ultrasound_request(request, pk):
    ultrasound_request = UltrasoundRequestForm(request.POST)
    print(ultrasound_request.is_valid())
    patient = Patient.objects.get(id=pk)
    staff = Staff.objects.get(basic_id=request.user.id)
    hospital = staff.hospital
    context = {'patient': patient, 'staff': staff, 'hospital': hospital}
    if ultrasound_request.is_valid():
        ultrasound_request.save_ultrasound_request(context)
        # nxt = request.POST.get('next', '/')
        return redirect('radiology_request_url', pk)
    else:
        print(ultrasound_request.errors)


def view_lab_result_waiting_list(request):
    context={}
    return render(request, "physician/forms/lab_result_waiting_list.html", context)


def view_radiology_result_waiting_list(request):
    context = {}
    return render(request, "physician/forms/radiology_result_wating_list.html", context)


def patient_radiology_result_detail(request):
    context = {}
    return render(request, "physician/forms/Patient_radiology_result.html", context)


def medical_history(request):
    context = {}
    return render(request, "physician/forms/medical_history.html", context)