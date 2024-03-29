from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from accounts.models import User, Hospital, Pharmacy, Staff
from login import decorators
from patient.models import Patient
from pharmacist.forms import Medication_Form
from physician.models import Appointment, Referral
from receptionist.models import Triage

@login_required(login_url='login_url')
@decorators.allowed_users(allowed_roles=['hospital admin'])
def search_staff(request):
    search_query = request.GET.get('search')
    try:
        staff = Staff.objects.get(basic_id=User.objects.get(username=search_query).id,
                                  hospital_id=Hospital.objects.get(admin_id=request.user.id).id)
        found = 'True'
        context = {'user_profile': staff.basic, 'found': found}
        return render(request, 'profiles/hospital_admin_users_profile.html', context)

        '''profile = User.objects.get(username=search_query)
        if request.user.role == 'hospital admin':
            hospital_id = Hospital.objects.get(admin_id=request.user.id).id
            user = Staff.objects.get(basic_id=profile.id)
            if user.hospital_id == hospital_id:
                found = 'True'
                context = {'user_profile': profile, 'found': found}
                return render(request, 'profiles/hospital_admin_users_profile.html', context)
            else:
                notfound = 'True'
                searched = 'Staff'
                context = {'searched': searched, 'notfound': notfound, 'search_query': search_query}
                return render(request, 'profiles/hospital_admin_users_profile.html', context)'''

    except:
        notfound = 'True'
        searched = 'Staff'
        context = {'searched': searched, 'notfound': notfound, 'search_query': search_query}
        return render(request, 'profiles/hospital_admin_users_profile.html', context)

@login_required(login_url='login_url')
@decorators.allowed_users(allowed_roles=['pharmacy admin'])
def search_pharmacist(request):
    search_query = request.GET.get('search')
    try:
        user = Receptionist.objects.get(basic_id=User.objects.get(username=search_query).id)
        pharmacy_id = Pharmacy.objects.get(admin_id=request.user.id).id
        if user.pharmacy_id == pharmacy_id:
            found = 'True'
            context = {'user_profile': user, 'found': found}
            return render(request, 'profiles/hospital_admin_users_profile.html', context)
        else:
            notfound = 'True'
            searched = 'Staff'
            context = {'searched': searched, 'notfound': notfound, 'search_query': search_query}
            return render(request, 'profiles/hospital_admin_users_profile.html', context)

    except:
        notfound = 'True'
        searched = 'Staff'
        context = {'searched': searched, 'notfound': notfound, 'search_query': search_query}
        return render(request, 'profiles/hospital_admin_users_profile.html', context)

@login_required(login_url='login_url')
@decorators.allowed_users(allowed_roles=['Receptionist','Nurse'])
def search_patient(request):
    search_query = request.GET.get('search')
    print(search_query)
    try:
        patient = Patient.objects.get(basic_id=User.objects.get(username=search_query).id)
        found = True
        appointment=Appointment.objects.filter(patient_id=patient.id,status="pending")
        referral=Referral.objects.filter(patient_id=patient.id,status="pending")
        try:
            registerd=Triage.objects.get(id=patient.id,status="pending")
        except:
            registerd=None
        print()
        print(appointment)
        print(referral)

        context = {'found': found,'user_profile': patient,'appointment':appointment,'referral':referral,'registered':registerd}
        return render(request, 'profiles/receptionist_patient_profile.html', context)
    except:
        notfound = True
        searched = 'patient'
        context = {'searched': searched, 'search_query': search_query, 'notfound': notfound}
        return render(request, 'profiles/receptionist_patient_profile.html', context)

@login_required(login_url='login_url')
@decorators.allowed_users(allowed_roles=['system admin'])
def search_healthcare_provider(request):
    search_query = request.GET.get('search')
    try:
        hospital = Hospital.objects.get(name__exact=search_query)
        found = 'True'
        context = {'hospital': hospital, 'found': found}
        return render(request, 'system_admin/hospital_profile.html', context)
    except:
        notfound = 'True'
        searched = "Hospital"
        context = {'searched': searched, 'notfound': notfound, 'search_query': search_query}
        return render(request, 'system_admin/hospital_profile.html', context)

@login_required(login_url='login_url')
@decorators.allowed_users(allowed_roles=['hospital admin'])
def search_nurse(request):
    search_query = request.GET.get('search')
    try:
        staff = Staff.objects.get(basic_id=User.objects.get(username=search_query).id,
                                  hospital_id=Hospital.objects.get(admin_id=request.user.id).id, )
        if staff.basic.role == 'Nurse':
            found = 'True'
            context = {'user_profile': staff.basic, 'found': found}
            return render(request, 'profiles/hospital_admin_users_profile.html', context)
        else:
            notfound = 'True'
            searched = 'Staff'
            context = {'searched': searched, 'notfound': notfound, 'search_query': search_query}
            return render(request, 'profiles/hospital_admin_users_profile.html', context)

    except:
        notfound = 'True'
        searched = 'Staff'
        context = {'searched': searched, 'notfound': notfound, 'search_query': search_query}
        return render(request, 'profiles/hospital_admin_users_profile.html', context)

@login_required(login_url='login_url')
@decorators.allowed_users(allowed_roles=['hospital admin'])
def search_physician(request):
    search_query = request.GET.get('search')
    try:
        staff = Staff.objects.get(basic_id=User.objects.get(username=search_query).id,
                                  hospital_id=Hospital.objects.get(admin_id=request.user.id).id, )
        if staff.basic.role == 'Physician':
            found = 'True'
            context = {'user_profile': staff.basic, 'found': found}
            return render(request, 'profiles/hospital_admin_users_profile.html', context)
        else:
            notfound = 'True'
            searched = 'Staff'
            context = {'searched': searched, 'notfound': notfound, 'search_query': search_query}
            return render(request, 'profiles/hospital_admin_users_profile.html', context)

    except:
        notfound = 'True'
        searched = 'Staff'
        context = {'searched': searched, 'notfound': notfound, 'search_query': search_query}
        return render(request, 'profiles/hospital_admin_users_profile.html', context)

@login_required(login_url='login_url')
@decorators.allowed_users(allowed_roles=['hospital admin'])
def search_radiologist(request):
    search_query = request.GET.get('search')
    try:
        staff = Staff.objects.get(basic_id=User.objects.get(username=search_query).id,
                                  hospital_id=Hospital.objects.get(admin_id=request.user.id).id)
        if staff.basic.role == 'Radiologist':
            found = 'True'
            context = {'user_profile': staff.basic, 'found': found}
            return render(request, 'profiles/hospital_admin_users_profile.html', context)
        else:
            notfound = 'True'
            searched = 'Staff'
            context = {'searched': searched, 'notfound': notfound, 'search_query': search_query}
            return render(request, 'profiles/hospital_admin_users_profile.html', context)

    except:
        notfound = 'True'
        searched = 'Staff'
        context = {'searched': searched, 'notfound': notfound, 'search_query': search_query}
        return render(request, 'profiles/hospital_admin_users_profile.html', context)

@login_required(login_url='login_url')
@decorators.allowed_users(allowed_roles=['hospital admin'])
def search_lab_technician(request):
    search_query = request.GET.get('search')
    try:
        staff = Staff.objects.get(basic_id=User.objects.get(username=search_query).id,
                                  hospital_id=Hospital.objects.get(admin_id=request.user.id).id)
        if staff.basic.role == 'Lab_technician':
            found = 'True'
            context = {'user_profile': staff.basic, 'found': found}
            return render(request, 'profiles/hospital_admin_users_profile.html', context)
        else:
            notfound = 'True'
            context = {'notfound': notfound, 'search_query': search_query}
            return render(request, 'profiles/hospital_admin_users_profile.html', context)

    except:
        notfound = 'True'
        searched = 'Staff'
        context = {'searched': searched, 'notfound': notfound, 'search_query': search_query}
        return render(request, 'profiles/hospital_admin_users_profile.html', context)

@login_required(login_url='login_url')
@decorators.allowed_users(allowed_roles=['pharmacist'])
def pharmacist_search_patient(request):
    medication=Medication_Form()
    search_query = request.GET.get('search')
    print(search_query)
    try:
        patient = Patient.objects.get(basic_id=User.objects.get(username=search_query).id)
        found = True

        context = {'found': found, 'user_profile': patient,'medication':medication}
        return render(request, 'profiles/pharmacist_patient_profile.html', context)
    except:
        notfound = True
        searched = 'patient'
        context = {'searched': searched, 'search_query': search_query, 'notfound': notfound,'medication':medication}
        return render(request, 'profiles/pharmacist_patient_profile.html', context)