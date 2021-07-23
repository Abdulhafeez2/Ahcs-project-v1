from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from hospital_admin.forms import *
# from xhtml2pdf import pisa
from login.models import User


# Create your views here.


@login_required(login_url='login_url')
# @decorators.allowed_users(allowed_roles=['Receptionist'])
# @decorators.receptionistonly
def receptionist_dashboard(request):
    context = {}
    return render(request, "receptionist/receptionist_dashboard.html", context)


def register_new_patient(request):
    if request.method == 'POST':
        form = User_registeration_Form(request.POST)
        print("pp")

        if form.is_valid():
            print('form is valid')
            new_user = form.save_patient()
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
        form = User_registeration_Form()
    context = {'form': form}
    return render(request, 'receptionist/form/registeration_form.html', context)


def receptionist_profile(request, pk):
    profile = User.objects.get(id=pk)
    # info = UserInfo.objects.get(user_id=pk)
    print(profile)
    context = {'user_profile': profile}

    return render(request, 'receptionist/user_profile.html', context)


def patient_profile(request, pk):
    profile = User.objects.get(id=pk)
    # info = UserInfo.objects.get(user_id=pk)
    print(profile)
    context = {'patient': profile}

    return render(request, 'receptionist/patient_profile.html', context)


def search_patient(request):
    search_query = request.GET.get('search', '')
    print(search_query)
    if search_query:


            try :
                patient = User.objects.get(username__exact=search_query, is_Patient=True)
                context = {'patient': patient}
                print(patient)
                return render(request, 'receptionist/form/search_result.html', context)
            except :
                return render(request, 'receptionist/form/patient_not_found.html')

    ## group=request.user.groups.all()[0].name

    ##else:
