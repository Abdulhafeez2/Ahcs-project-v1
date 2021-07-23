from django.shortcuts import render

# Create your views here.
def pharmacist_homepage(request):

    context={}
    return render(request,'pharmacist/pharmacist_homepage.html',context)