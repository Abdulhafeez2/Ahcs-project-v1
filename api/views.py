from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.models import User
from .models import Note
from .serializers import *
from patient.models import Medication, Patient
from physician.models import Appointment


@api_view(['GET'])

def getRoutes(request):
    routes=[

        {
            'Endpoint':'/notes/',
            'method':'GET',
            'body':None,
            'descripion':'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'descripion': 'Returns a single note'

        },
        {
            'Endpoint': '/notes/create/',
            'method': 'GET',
            'body': None,
            'descripion': 'create a new note'
        }
    ]
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes=Note.objects.all()
    serializer=NoteSerializer(notes,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request,pk):
    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(notes, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createNote(request):
    data=request.data
    note=Note.objects.create(
        body=data['body']
    )
    serializer= NoteSerializer(note,many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateNote(request,pk):
    data=request.data
    note=Note.objects.get(id=pk)
    serializer= NoteSerializer(note,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])

def deleteNote(reqeust,pk):
    note=Note.objects.get(id=pk)
    note.delete()

    return Response("Note deleted successfully")


@api_view(['GET'])

def getMedication(request,username):
    medications=Medication.objects.filter(patient_id=Patient.objects.get(basic_id=User.objects.get(username=username).id))
    serializer=MedicationSerializer(medications,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def  getAppointment(request,username):
    appointment=Appointment.objects.filter(patient_id=Patient.objects.get(basic_id=User.objects.get(username=username).id))
    serializer=AppointmentSerializer(appointment,many=True)
    return Response(serializer.data)