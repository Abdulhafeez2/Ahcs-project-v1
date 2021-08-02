from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from hospital_admin.forms import *
# from xhtml2pdf import pisa
from accounts.models import User


# Create your views here.


@login_required(login_url='login_url')
# @decorators.allowed_users(allowed_roles=['Receptionist'])
# @decorators.receptionistonly
def receptionist_dashboard(request):
    context = {}
    return render(request, "receptionist/homepage.html", context)


def register_new_patient(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print('form is valid')
            hospital = Receptionist.objects.get(basic_id=request.user.id).hospital.id
            context = {'hospital': hospital}
            new_user = form.save_patient(context)
            context = {'username': new_user['username'], 'password': new_user['password']}
            '''template_path = 'receptionist/credentials.html'
            # Create a Django response object, and specify content_type as pdf
            response = HttpResponse(content_type='application/pdf')
            ## if want to download it
            ##response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            ## if want to display it
            response['Content-Disposition'] = 'filename=context["username"].pdf'
            # find the template and render it.
            template = get_template(template_path)
            html = template.render(context)
            # create a pdf
            pisa_status = pisa.CreatePDF(html, dest=response)
            # if error then show some funy view
            if pisa_status.err:
                return HttpResponse('We had some errors <pre>' + html + '</pre>')
            return response'''
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'receptionist/form/registeration_form.html', context)


def patient_profile(request, pk):
    profile = User.objects.get(id=pk)
    # info = UserInfo.objects.get(user_id=pk)
    print(profile)
    context = {'patient': profile}
    return render(request, 'receptionist/patient_profile.html', context)




    ## group=request.user.groups.all()[0].name

    ##else:
