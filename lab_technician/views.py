import datetime

from django.shortcuts import render, redirect

# Create your views here.
from accounts.models import Hospital, Staff
from lab_technician.forms import StoolResultForm, UrineResultForm, HematologyResultForm
from lab_technician.models import UrineAnalysisWaitingList, HematologyWaitingList
from patient.models import Hematology, UrineAnalysis, StoolExamination, Patient


def lab_technician_homepage(request):
    hospital = Hospital.objects.get(id=Staff.objects.get(basic_id=request.user.id).hospital_id)
    staff = Staff.objects.get(basic_id=request.user.id)
    context = {}
    hematology = Hematology.objects.filter(hospital_id=hospital.id, requested_to_id=staff.id,
                                           status='pending')
    if hematology.all:
        context['hematology'] = hematology
    urine = UrineAnalysis.objects.filter(hospital_id=hospital.id, requested_to_id=staff.id,
                                         status='pending')
    if urine.all:
        context['urine'] = urine
    stool = StoolExamination.objects.filter(hospital_id=hospital.id, requested_to_id=staff.id,
                                            status='pending')
    if stool.all:
        context['stool'] = stool

    return render(request, 'lab_technician/homepage.html', context)


def view_lab_request_detail(request, pk):
    hospital = Hospital.objects.get(id=Staff.objects.get(basic_id=request.user.id).hospital_id)
    staff = Staff.objects.get(basic_id=request.user.id)
    context = {}
    try:
        hematology = Hematology.objects.get(hospital_id=hospital.id, requested_to_id=staff.id, patient_id=pk,
                                            status='pending')
        print(hematology)
        context['hematology'] = hematology
    except:
        not_found = True
    try:
        urine = UrineAnalysis.objects.get(hospital_id=hospital.id, requested_to_id=staff.id, patient_id=pk,
                                          status='pending')
        context['urine'] = urine
        print(urine)
    except:
        not_found = True
    try:
        stool = StoolExamination.objects.get(hospital_id=hospital.id, requested_to_id=staff.id, patient_id=pk,
                                             status='pending')
        if stool:
            context['stool'] = stool
            print(stool)
    except:
        not_found = True
    context["stool_result_form"] = StoolResultForm(instance=pk)
    context["urine_result_form"] = UrineResultForm(instance=pk)
    context["hematology_result_form"] = HematologyResultForm(instance=pk)
    context['user_profile'] = Patient.objects.get(id=pk)
    return render(request, "lab_technician/form/view_request.html", context)


def add_stool_result(request, pk):
    if request.method == 'POST':
        stool = StoolResultForm(request.POST, instance=pk)
        staff = Staff.objects.get(basic_id=request.user.id)
        hospital = staff.hospital

        rqst = StoolExamination.objects.get(hospital_id=hospital.id, requested_to_id=staff.id,
                                            patient_id=pk, status='pending')

        if stool.is_valid():
            for s in stool:
                setattr(rqst, s.name, stool.cleaned_data.get(s.name))

            rqst.date_of_report = datetime.datetime.now()
            rqst.reported_by_id = staff.id
            rqst.status = 'reported'
            rqst.save()
            return redirect('request_detail_url', pk)


def add_urine_result(request, pk):
    if request.method == 'POST':
        urine = UrineResultForm(request.POST, instance=pk)
        staff = Staff.objects.get(basic_id=request.user.id)
        hospital = staff.hospital

        rqst = UrineAnalysis.objects.get(hospital_id=hospital.id, requested_to_id=staff.id,
                                         patient_id=pk, status='pending')
        waiting = UrineAnalysisWaitingList.objects.get(hospital_id=hospital.id, requested_to_id=staff.id,
                                                       patient_id=pk, status='pending')

        if urine.is_valid():
            for s in urine:
                setattr(rqst, s.name, urine.cleaned_data.get(s.name))

            rqst.date_of_report = datetime.datetime.now()
            rqst.reported_by_id = staff.id
            rqst.status = 'reported'
            rqst.save()
            waiting.status = 'reported'
            waiting.save()
            return redirect('request_detail_url', pk)


def add_hematology_result(request, pk):
    if request.method == 'POST':
        hematology = HematologyResultForm(request.POST, instance=pk)
        staff = Staff.objects.get(basic_id=request.user.id)
        hospital = staff.hospital

        rqst = Hematology.objects.get(hospital_id=hospital.id, requested_to_id=staff.id,
                                      patient_id=pk, status='pending')
        waiting = HematologyWaitingList.objects.get(hospital_id=hospital.id, requested_to_id=staff.id,
                                                    patient_id=pk, status='pending')

        if hematology.is_valid():
            for s in hematology:
                setattr(rqst, s.name, hematology.cleaned_data.get(s.name))

            rqst.date_of_report = datetime.datetime.now()
            rqst.reported_by_id = staff.id
            rqst.status = 'reported'
            rqst.save()
            waiting.status = 'reported'
            waiting.save()
            return redirect('request_detail_url', pk)


def remove_from_list(request, pk):
    hospital = Hospital.objects.get(id=Staff.objects.get(basic_id=request.user.id).hospital_id)
    staff = Staff.objects.get(basic_id=request.user.id)

    rqst = StoolExamination.objects.get(hospital_id=hospital.id, requested_to_id=staff.id,
                                        patient_id=pk, status='pending')
    rqst.status = 'reported'
    staff.num_waiting = staff.num_waiting - 1
    rqst.save()
    staff.save()

    return redirect('lab_technician/lab_technician_homepage_url')
