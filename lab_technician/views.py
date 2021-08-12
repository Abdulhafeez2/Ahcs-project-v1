from django.shortcuts import render


# Create your views here.
def lab_technician_homepage(request):
    try:
        #request_list = Triage.objects.filter(hospital_id=Staff.objects.get(basic_id=request.user.id).hospital_id,
                                     #      status='pending')
        list = True
        context = {'list': list}
        return render(request, "lab_technician/homepage.html", context)
    except:
        #list = False
        context = {'list': list}
        return render(request, "lab_technician/homepage.html", context)


def view_reqeust(request):
    context={}
    return render(request, "lab_technician/form/view_request.html", context)