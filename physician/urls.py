from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.physician_homepage, name="physician_homepage_url"),
    path('view_waiting_list/', views.view_waiting_list, name='view_waiting_list'),
    path('add_prescription/', views.add_prescription, name='add_prescription'),
    path('radiology_request/', views.add_radiology_request, name='radiology_request_url'),
    path('lab_request/', views.lab_request, name='lab_request_url'),
    path('patient_detail/<str:pk>/', views.patient_detail, name='patient_detail_url'),
]

