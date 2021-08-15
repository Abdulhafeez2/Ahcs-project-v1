from django.shortcuts import render

# Create your views here.
def radiologist_homepage(request):
    context={}
    return render(request,'homepage.html',context)


def request_detail(request):
    context = {}
    return render(request, 'radiologist/patient_detail.html', context)