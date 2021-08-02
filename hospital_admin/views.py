from django.shortcuts import render
from accounts.models import User
from login import decorators
from .forms import *


## from django.template.loader import render_to_string
## import weasyprint
# from xhtml2pdf import pisa


# @decorators.hospital_adminonly
def hospital_admin_homepage(request):
    hospital = Hospital.objects.get(admin=request.user.id)
    context = {'hospital_name': hospital}
    return render(request, 'hospital_admin/homepage.html', context)


##############################################################################################################################################

def add_new_user(request):
    msg = None
    if request.method == 'POST':

        form = UserRegistrationForm(request.POST)
        hospital = Hospital.objects.get(admin_id=request.user.id)
        context = {'hospital': hospital}
        if form.is_valid():
            new_user = form.save(context)

            msg = "Staff registered"
            context = {'username': new_user['username'], 'password': new_user['password']}
            # template_path = 'hospital_admin/credentials.html'
            # Create a Django response object, and specify content_type as pdf
            # response = HttpResponse(content_type='application/pdf')
            ## if want to download it
            ##response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            ## if want to display it
            # response['Content-Disposition'] = 'filename=context["username"].pdf'
            # find the template and render it.
            # template = get_template(template_path)
            # html = template.render(context)
            # create a pdf
        # pisa_status = pisa.CreatePDF(html, dest=response)
        # if error then show some funy view
        # if pisa_status.err:
        # return HttpResponse('We had some errors <pre>' + html + '</pre>')
        # return response
    else:
        form = UserRegistrationForm

    context = {'form': form}
    return render(request, 'hospital_admin/receptionists_add.html', context)


################################################################################

# all users
def all_users(request):
    hospital_id = Hospital.objects.get(admin_id=request.user.id).id
    receptionists = Receptionist.objects.filter(hospital_id=hospital_id)
    '''physician = Physician.objects.filter(hospital_id=hospital_id)
    Lab_technician = LabTechnician.objects.filter(hospital_id=hospital_id)
    nurse = Nurse.objects.filter(hospital_id=hospital_id)
    nurse = Radiologist.objects.filter(hospital_id=hospital_id)'''
    context = {'receptionists': receptionists}
    return render(request, 'forms/all_users.html', context)


def all_physicians(request):
    physicians = User.objects.filter(role='Physician')
    context = {'all_physicians': physicians}
    return render(request, 'forms/all-physicians.html', context)


def all_nurses(request):
    nurses = User.objects.filter(role='Nurse')
    context = {'all_nurses': nurses}
    return render(request, 'forms/all-nurses.html', context)


def all_radiologists(request):
    radiologists = User.objects.filter(role='Radiologist')
    context = {'all_radiologists': radiologists}
    return render(request, 'forms/all-radiologists.html', context)


def all_lab_technicians(request):
    all_lab_technicians = User.objects.filter(role='Lab_technician')
    context = {'all_lab_technicians': all_lab_technicians}
    return render(request, 'forms/all-lab_technicians.html', context)


def all_pharmacists(request):
    all_lab_technician = User.objects.filter(role='Pharmacist')
    context = {'all_pharmacists': all_pharmacists}
    return render(request, 'forms/all-pharmacists.html', context)


def all_receptionists(request):
    hospital_id = Hospital.objects.get(admin_id=request.user.id).id
    receptionists = Receptionist.objects.filter(hospital_id=hospital_id)
    context = {'receptionists': receptionists}
    return render(request, 'forms/all_receptionists.html', context)
