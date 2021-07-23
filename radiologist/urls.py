from django.urls import path
from . import views


urlpatterns = [
    path('',views.radiologist_homepage,name='radiologist_homepage_url'),

]
