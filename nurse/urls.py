from django.urls import path
from . import views


urlpatterns = [
    path('',views.nurse_homepage,name='nurse_homepage_url'),
    path('add_vital_sign/',views.add_vital_sign,name='add_vital_sign'),
]
