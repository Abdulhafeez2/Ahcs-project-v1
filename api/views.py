from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import MedicationSerializer, PaitentSerializer, UserSerializer
from patient.models import Medication, Patient

from accounts.models import User


@api_view(['GET'])
def get_medications(request):
    medication = Medication.objects.all()
    serializer = MedicationSerializer(medication, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_medication(request, pk):
    medication = Medication.objects.filter(patient_id=pk)
    patient = Patient.objects.get(id=pk)
    user=User.objects.get(id=patient.basic_id)
    serializer = MedicationSerializer(medication,many=True)
    user_serializer=UserSerializer(user,many=False)
    return Response(serializer.data)
