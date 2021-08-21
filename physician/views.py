import datetime
from time import timezone

from django import forms
from django.contrib import messages
from django.shortcuts import render, redirect

from accounts.models import Staff, User, Hospital
from lab_technician.models import UrineAnalysisWaitingList, HematologyWaitingList
from login import urls
from django.contrib.auth.decorators import login_required
from login import decorators
# Create your views here.

# @login_required(login_url='login_url')
# @decorators.physicianonly
from patient.models import Patient, VitalSign, PatientForm, UltraSound, XrayExamination, StoolExamination, \
    UrineAnalysis, Hematology
from physician.forms import AddPatientForm, ReferralRequestForm, PrescriptionForm, AdministeredTreatmentForm, \
    XrayRequestForm, UltrasoundRequestForm, UrineAnalysisRequestForm, StoolExaminationRequestForm, \
    HematologyExaminationRequestForm, AppointmentForm, DateForm
from physician.models import PatientWaitingList, Referral, Appointment


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
    messages.success(request, "Removed from list")
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
    appointment_form=AppointmentForm

    hospital_id = Staff.objects.get(basic_id=request.user.id).hospital.id
    referral_request = ReferralRequestForm(pk=hospital_id)

    administered_treatment = AdministeredTreatmentForm
    context = {'patient': pk, 'user_profile': user_profile, 'vital_sign': vital_sign,
               'patient_form': patient_form, 'prescription_form': prescription_form,
               'referral': referral, 'referral_request': referral_request,
               'latest_patient_form': latest_patient_form,
               'administered_treatment': administered_treatment,'appointment_form':appointment_form}
    return render(request, "physician/patient_detail.html", context)


def lab_request(request, pk):
    urine_analysis = UrineAnalysisRequestForm
    stool = StoolExaminationRequestForm
    hematology = HematologyExaminationRequestForm
    context = {'urine_analysis': urine_analysis, 'stool': stool, 'hematology': hematology, 'pk': pk}
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
            messages.success(request, "Patient form updated")
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
            messages.success(request, "Referral request sent successfully")
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
            messages.success(request, "Prescription added Successfully")
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
            messages.success(request, "Treatment Added Successfully")
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
            messages.success(request, "Request Sent ")
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
        messages.success(request, "Staff registered Successfully")
        # nxt = request.POST.get('next', '/')
        return redirect('radiology_request_url', pk)
    else:
        print(ultrasound_request.errors)


def view_lab_result_waiting_list(request):
    hospital = Hospital.objects.get(id=Staff.objects.get(basic_id=request.user.id).hospital_id)
    staff = Staff.objects.get(basic_id=request.user.id)
    specialty = staff.specialty
    if specialty == 'Ultrasound':
        report = UltraSound.objects.get(hospital_id=hospital.id, requested_by_id=staff.id, status='reported')
    elif specialty == 'X-ray':
        report = XrayExamination.objects.get(hospital_id=hospital.id, requested_by_id=staff.id, status='reported')

    context = {}
    return render(request, "physician/forms/lab_result_waiting_list.html", context)


def view_radiology_result_waiting_list(request):
    hospital = Hospital.objects.get(id=Staff.objects.get(basic_id=request.user.id).hospital_id)
    staff = Staff.objects.get(basic_id=request.user.id)
    reports = {}
    ultra_report = UltraSound.objects.filter(hospital_id=hospital.id, requested_by_id=staff.id, status='reported')
    if ultra_report.all:
        reports['ultra'] = ultra_report
    xray_report = XrayExamination.objects.filter(hospital_id=hospital.id, requested_by_id=staff.id, status='reported')
    if xray_report.all:
        reports['xray'] = 'xray_report'
    context = {'ultra_report': ultra_report, 'xray_report': xray_report, 'reports': reports}
    return render(request, "physician/forms/radiology_result_wating_list.html", context)


def patient_radiology_result_detail(request, pk):
    hospital = Hospital.objects.get(id=Staff.objects.get(basic_id=request.user.id).hospital_id)
    staff = Staff.objects.get(basic_id=request.user.id)
    ultra_report = UltraSound.objects.filter(hospital_id=hospital.id, requested_by_id=staff.id, status='reported', patient_id=pk)
    xray_report = XrayExamination.objects.filter(hospital_id=hospital.id, requested_by_id=staff.id, status='reported', patient_id=pk)
    context = {'ultra_report': ultra_report, 'xray_report': xray_report, 'pk': pk}
    return render(request, "physician/forms/Patient_radiology_result.html", context)


def medical_history(request):
    context = {}
    return render(request, "physician/forms/medical_history.html", context)


def add_stool_examination_request(request, pk):
    if request.method == 'POST':
        stool = StoolExaminationRequestForm(request.POST)
        patient = Patient.objects.get(id=pk)
        staff = Staff.objects.get(basic_id=request.user.id)
        hospital = staff.hospital
        context = {'patient': patient, 'staff': staff, 'hospital': hospital}
        if stool.is_valid():
            lab_technician = Staff.objects.filter(hospital_id=context['hospital'].id, specialty='Lab_technician'). \
                order_by('-num_waiting').last()
            stool_request = StoolExamination.objects.create(
                patient_id=patient.id,
                requested_by_id=staff.id,
                requested_to_id=lab_technician.id,
                hospital_id=hospital.id,
            )
            for s in stool:
                if stool.cleaned_data.get(s.name):
                    setattr(stool_request, s.name, 'requested')
            stool_request.save()
            lab_tech = Staff.objects.get(id=lab_technician.id)
            lab_tech.num_waiting = staff.num_waiting + 1
            lab_tech.save()
            messages.success(request, "Request Sent")
            return redirect('lab_request_url', pk)


def add_urine_analysis_request(request, pk):
    if request.method == 'POST':
        urine_analysis = UrineAnalysisRequestForm(request.POST)
        patient = Patient.objects.get(id=pk)
        staff = Staff.objects.get(basic_id=request.user.id)
        hospital = staff.hospital
        context = {'patient': patient, 'staff': staff, 'hospital': hospital}
        if urine_analysis.is_valid():
            lab_technician = Staff.objects.filter(hospital_id=context['hospital'].id, specialty='Lab_technician'). \
                order_by('-num_waiting').last()
            urine_analysis_object = UrineAnalysis.objects.create(
                patient_id=patient.id,
                requested_by_id=staff.id,
                requested_to_id=lab_technician.id,
                hospital_id=hospital.id,
            )
            urine_rqst = UrineAnalysisWaitingList.objects.create(
                patient_id=patient.id,
                requested_by_id=staff.id,
                requested_to_id=lab_technician.id,
                hospital_id=hospital.id,
            )
            for urine in urine_analysis:
                if urine_analysis.cleaned_data.get(urine.name):
                    setattr(urine_rqst, urine.name, True)
            urine_analysis_object.save()
            urine_rqst.save()
            lab_tech = Staff.objects.get(id=lab_technician.id)
            lab_tech.num_waiting = staff.num_waiting + 1
            lab_tech.save()
            messages.success(request, "Request Sent")
            return redirect('lab_request_url', pk)


def add_hematology_request(request, pk):
    if request.method == 'POST':
        hematology_request = HematologyExaminationRequestForm(request.POST)
        patient = Patient.objects.get(id=pk)
        staff = Staff.objects.get(basic_id=request.user.id)
        hospital = staff.hospital
        context = {'patient': patient, 'staff': staff, 'hospital': hospital}
        if hematology_request.is_valid():
            lab_technician = Staff.objects.filter(hospital_id=context['hospital'].id, specialty='Lab_technician'). \
                order_by('-num_waiting').last()
            hematology_object = Hematology.objects.create(
                patient_id=patient.id,
                requested_by_id=staff.id,
                requested_to_id=lab_technician.id,
                hospital_id=hospital.id,
            )
            hematology_rqst = HematologyWaitingList.objects.create(
                patient_id=patient.id,
                requested_by_id=staff.id,
                requested_to_id=lab_technician.id,
                hospital_id=hospital.id,
            )
            for hematology in hematology_request:
                if hematology_request.cleaned_data.get(hematology.name):
                    setattr(hematology_rqst, hematology.name, True)
            hematology_object.save()
            hematology_rqst.save()
            lab_tech = Staff.objects.get(id=lab_technician.id)
            lab_tech.num_waiting = staff.num_waiting + 1
            lab_tech.save()
            messages.success(request, "Request Sent")
            return redirect('lab_request_url', pk)

def add_appointment(request,pk):
    if request.method=='POST':
        patient = Patient.objects.get(id=pk)
        staff = Staff.objects.get(basic_id=request.user.id)
        hospital = staff.hospital
        context = {'patient': patient, 'staff': staff, 'hospital': hospital}
        appointment_form=AppointmentForm(request.POST)
        if appointment_form.is_valid():
            appointment_form.save_appointment(context)
            messages.success(request, "Appointement Added Successfully")
            return redirect('patient_detail_url', pk)


