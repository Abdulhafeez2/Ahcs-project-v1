from django.db import models
from accounts.models import User, Hospital, Staff


# Create your models here.
from patient.models import Patient


class PatientWaitingList(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    physician = models.ForeignKey(Staff, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.patient


class Appointment(models.Model):
    physician = models.ForeignKey(Staff, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    given_date = models.DateTimeField()
    appointment_date = models.DateTimeField()
    case = models.CharField(max_length=50)
    status = models.CharField(max_length=50)


class Referral(models.Model):
    referred_by = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='referred_by')
    referred_to = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    referred_on_date = models.DateTimeField()
    approved_on_date = models.DateTimeField(default='Null')
    case = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    approved_by = models.ForeignKey(Staff, on_delete=models.CASCADE, default='NuLL', related_name='approved_by')
