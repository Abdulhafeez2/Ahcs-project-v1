from django.urls import path
from . import  views

urlpatterns=[
    #path('profile/<str:pk>',views.user_profile,name='user_profile_url'),
    path('my_profile/<str:pk>',views.my_profile,name='my_profile_url'),
]