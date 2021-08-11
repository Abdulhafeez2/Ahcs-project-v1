from django.urls import path
from . import views


urlpatterns = [
    path('', views.lab_technician_homepage, name='lab_technician_homepage_url'),
    path('view_request', views.view_reqeust, name='view_request_url'),

]
