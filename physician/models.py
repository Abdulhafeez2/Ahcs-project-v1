from datetime import timezone, datetime

from django.db import models
from accounts.models import Hospital, Staff


# Create your models here.
from patient.models import Patient


class PatientWaitingList(models.Model):
    added_by = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='added_by')
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    physician = models.ForeignKey(Staff, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient


class Appointment(models.Model):
    physician = models.ForeignKey(Staff, on_delete=models.CASCADE,)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,)
    given_date = models.DateTimeField(default=datetime.now())
    appointment_date = models.DateTimeField()
    case = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    added_time=models.DateTimeField(auto_now_add=True)



class Referral(models.Model):
    referred_by = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='referred_by')
    referred_to = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    referred_on_date = models.DateTimeField()
    approved_on_date = models.DateTimeField(default='Null')
    case = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    approved_by = models.ForeignKey(Staff, on_delete=models.CASCADE, default='NuLL', related_name='approved_by')
