from django.urls import path
from . import views



urlpatterns=[
    path('',views.getRoutes),
    path('notes/',views.getNotes),
    path('<str:pk>/update/',views.updateNote),
    path('<str:pk>/delete/',views.deleteNote),
    path('create_note',views.createNote),
    path('notes/<str:pk>/',views.getNote),
    path('check/<str:username>/<str:password>/',views.check),
    path('get_medications/<str:username>/',views.getMedication),
    path('get_appointment/<str:username>/', views.getAppointment)

]