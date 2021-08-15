from django.urls import path

from api import views

urlpatterns = [
    path('get_medication/<str:pk>/', views.get_medication),
    path('get_medications/', views.get_medications)
]
