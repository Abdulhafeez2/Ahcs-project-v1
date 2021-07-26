from . import views
from django.urls import path

urlpatterns = [
    path('search/', views.search_staff, name='search_staff_url'),
]
