from django.shortcuts import render
from login.models import User
# Create your views here.

def user_profile(request,pk):
    user=User.object.get(id=pk)

    context={}
    return render(request,"profiles/user_profile.html",context)




def my_profile(request,pk):
    context={}
    return render(request,"profiles/user_profile.html",context)