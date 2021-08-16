from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.physician_homepage, name="physician_homepage_url"),
    path('view_waiting_list/', views.view_waiting_list, name='view_waiting_list'),
    path('add_prescription/', views.add_prescription, name='add_prescription'),
    path('radiology_request/<str:pk>/', views.radiology_requests, name='radiology_request_url'),
    path('xray_request/<str:pk>/', views.add_xray_request, name='add_xray_request_url'),
    path('ultrasound_request/<str:pk>/', views.add_ultrasound_request, name='add_ultrasound_request_url'),
    path('lab_request/<str:pk>/', views.lab_request, name='lab_request_url'),
    path('patient_detail/<str:pk>/', views.patient_detail, name='patient_detail_url'),
    path('patient_form/<str:pk>/', views.add_patient_form, name='add_patient_form_url'),
    path('add_referral/<str:pk>/', views.add_referral, name='add_referral_url'),
    path('add_prescription/<str:pk>/', views.add_prescription, name='add_prescription_url'),
    path('remove_from_list/<str:pk>/', views.remove_from_list, name='remove_from_list_url'),
    path('add_administered_treatment/<str:pk>/', views.administered_treatment, name='add_administered_treatment_url'),
]

