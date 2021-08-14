from django.shortcuts import render

# Create your views here.
from accounts.models import Pharmacy


def pharmacist_homepage(request):

    return render(request, 'pharmacist/homepage.html')

