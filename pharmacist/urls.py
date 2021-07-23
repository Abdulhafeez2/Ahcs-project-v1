from django.urls import path
from . import views


urlpatterns = [
    path('',views.pharmacist_homepage,name='pharmacist_homepage_url'),

]
