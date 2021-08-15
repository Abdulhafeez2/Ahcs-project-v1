from rest_framework.serializers import ModelSerializer

from accounts.models import User
from patient.models import Medication, Patient


class MedicationSerializer(ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'

class PaitentSerializer(ModelSerializer):
    class Meta:
        model=Patient
        fields='__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields='__all__'