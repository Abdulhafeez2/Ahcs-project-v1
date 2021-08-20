from django.urls import path
from . import views


urlpatterns = [
    path('', views.pharmacist_homepage, name='pharmacist_homepage_url'),
    path('patient_detail/',views.patient_detail,name='patient_detail_url')

]
