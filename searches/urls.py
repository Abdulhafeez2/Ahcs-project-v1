from . import views
from django.urls import path

urlpatterns = [
    path('search_staff/', views.search_staff, name='search_staff_url'),
    path('search_healthcare_provider_url/', views.search_healthcare_provider, name='search_healthcare_provider_url'),
    path('search_patient/', views.search_patient, name='search_patient_url'),
]
