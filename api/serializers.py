from rest_framework.serializers import ModelSerializer
from . models import Note
from patient.models import Medication
from physician.models import Appointment

class NoteSerializer(ModelSerializer):
    class Meta:
        model=Note
        fields='__all__'

class MedicationSerializer(ModelSerializer):
    class Meta:
        model= Medication
        fields='__all__'

class AppointmentSerializer(ModelSerializer):
    class Meta:
        model=Appointment
        fields='__all__'