from django.shortcuts import render

from login.models import User
# Create your views here.

def user_profile(request,pk):
    user = User.objects.get(id=pk)

    context = {}
    return render(request, "profiles/user_profile.html", context)




def my_profile(request, pk):
    profile = User.objects.get(id=pk)
    role = request.user.role
    context = {'user_profile': profile, 'role': role}
    print(role)
    if profile.is_superuser:
        return render(request, 'profiles/system_admin_my_profile.html', context)
    if role == 'Hospital_admin':
        return render(request, 'profiles/hospital_admin_my_profile.html', context)
    if role == 'Physician':
        return render(request, 'profiles/physician_my_profile.html', context)
    if role == 'Receptionist':
        return render(request, 'profiles/receptionist_my_profile.html', context)
    if role == 'Lab_technician':
        return render(request, 'profiles/lab_technician_my_profile.html', context)
    if role == 'Nurse':
        return render(request, 'profiles/nurse_my_profile.html', context)

