from django.shortcuts import render

# Create your views here.
def radiologist_homepage(request):
    context={}
    return render(request,'radiologist/radiologist_homepage.html',context)