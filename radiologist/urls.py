from django.urls import path
from . import views


urlpatterns = [
    path('', views.radiologist_homepage, name='radiologist_homepage_url'),
    path('request_detail/<str:pk>/', views.request_detail, name='request_detail_url'),

]
