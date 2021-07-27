from django.shortcuts import render

# Create your views here.
from hospital_admin.forms import User_registeration_Form
from system_admin.forms import HealthCareProviderRegistrationForm


def homepage(request):
    context = {}
    return render(request, 'system_admin/homepage.html', context)


def add_new_healthcare_provider(request):
    msg = None
    if request.method == 'POST':

        form = HealthCareProviderRegistrationForm(request.POST)
        form1 = User_registeration_Form(request.POST)


        print(form1.errors)
        if form1.is_valid() and form.is_valid():

            new_healthcare_provider = form.save_health_care_provider()
            new_admin = form1.save_admin()

        else:

            form = HealthCareProviderRegistrationForm
            form1 = User_registeration_Form

    context = {'form': form, 'form1': form1}
    return render(request, 'system_admin/healthcare_provider_add.html', context)
