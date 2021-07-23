from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('',views.physician_homepage,name="physician_homepage_url"),
    path('view_waiting_list/',views.view_waiting_list,name='view_waiting_list'),
    path('add_prescription/',views.add_prescription,name='add_prescription'),
    path('xray_request/',views.add_xray_request,name='xray_request'),
]

