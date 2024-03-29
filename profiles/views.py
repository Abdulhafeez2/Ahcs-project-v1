from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from accounts.models import User
from hospital_admin.forms import UserRegistrationForm

# Create your views here.
from login.decorators import allowed_users


@login_required(login_url='login_url')
###############################################################
def user_profile(request, pk):
    profile = User.objects.get(id=pk)

    found = 'True'
    context = {'found': found, 'user_profile': profile,'form':form}
    if request.user.is_superuser:
        return render(request, 'profiles/system_admin_users_profile.html', context)
    elif request.user.role == 'hospital admin':
        return render(request, 'profiles/hospital_admin_users_profile.html', context)
    elif request.user.role == 'pharmacy admin':
        return render(request, 'profiles/system_admin_users_profile.html', context)
    elif request.user.role == 'Physician':
        return render(request, 'profiles/system_admin_users_profile.html', context)
    elif request.user.role == 'Receptionist':
        return render(request, 'profiles/system_admin_users_profile.html', context)
    elif request.user.role == 'Nurse':
        print(profile)
        return render(request, 'profiles/system_admin_users_profile.html', context)
    elif request.user.role == 'Lab Technician admin':
        return render(request, 'profiles/system_admin_users_profile.html', context)

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['*'])
def my_profile(request, pk):
    profile = User.objects.get(id=pk)
    appointment=None
    form=UserRegistrationForm()
    role = request.user.role
    if request.user.role == 'Physician':
        appointment=True
    context = {'user_profile': profile, 'role': role,'form':form,'appointment':appointment}
    print(role)
    if request.user.is_superuser:
        return render(request, 'profiles/system_admin_my_profile.html', context)
    elif role == 'hospital admin':
        return render(request, 'profiles/hospital_admin_my_profile.html', context)
    elif role == 'pharmacy admin':
        return render(request, 'profiles/pharmacy_admin_my_profile.html', context)
    elif role == 'pharmacist':
        return render(request, 'profiles/pharmacist_my_profile.html', context)
    elif role == 'Physician':

        return render(request, 'profiles/physician_my_profile.html', context)
    elif role == 'Receptionist':
        return render(request, 'profiles/receptionist_my_profile.html', context)
    elif role == 'Lab_technician':
        return render(request, 'profiles/lab_technician_my_profile.html', context)
    elif role == 'Nurse':
        return render(request, 'profiles/nurse_my_profile.html', context)
