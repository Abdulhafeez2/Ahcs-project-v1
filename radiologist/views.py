from django.shortcuts import render

# Create your views here.
from accounts.models import Hospital, Staff
from patient.models import UltraSound, XrayExamination, Patient


def radiologist_homepage(request):
    hospital = Hospital.objects.get(id=Staff.objects.get(basic_id=request.user.id).hospital_id)
    staff = Staff.objects.get(basic_id=request.user.id)
    specialty = staff.specialty
    if specialty == 'Ultrasound':
        try:
            request_list = UltraSound.objects.filter(hospital_id=hospital.id, requested_to_id=staff.id,
                                                     status='pending')
            rqst_list = True
            context = {'hospital': hospital, 'rqst_list': rqst_list, 'request_list': request_list}
            return render(request, 'homepage.html', context)
        except:
            rqst_list = False
            context = {'hospital': hospital, 'rqst_list': rqst_list}
            return render(request, 'homepage.html', context)
        context = {'hospital': hospital}

    elif specialty == 'X-ray':
        try:
            request_list = XrayExamination.objects.filter(hospital_id=hospital.id, requested_to_id=staff.id,
                                                          status='pending')
            rqst_list = True
            context = {'hospital': hospital, 'rqst_list': rqst_list, 'request_list': request_list}
            return render(request, 'homepage.html', context)
        except:
            rqst_list = False
            context = {'hospital': hospital, 'rqst_list': rqst_list}
            return render(request, 'homepage.html', context)


def request_detail(request, pk):
    hospital = Hospital.objects.get(id=Staff.objects.get(basic_id=request.user.id).hospital_id)
    staff = Staff.objects.get(basic_id=request.user.id)
    user_profile = Patient.objects.get(id=pk)
    specialty = staff.specialty
    rqst = None
    if specialty == 'Ultrasound':
        rqst = UltraSound.objects.get(hospital_id=hospital.id, requested_to_id=staff.id,
                                                     patient_id=pk, status='pending')
    elif specialty == 'X-ray':
        rqst = XrayExamination.objects.get(hospital_id=hospital.id, requested_to_id=staff.id,
                                              patient_id=pk, status='pending')

    context = {'hospital': hospital, 'specialty': specialty, 'user_profile': user_profile, 'rqst': rqst}
    return render(request, 'radiologist/request_detail.html', context)
