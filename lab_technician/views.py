from django.shortcuts import render

# Create your views here.
def lab_technician_homepage(request):
    context={}
    return render(request,'lab_technician/lab_technician_homepage.html',context)