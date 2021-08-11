from django.db import models

# Create your models here.
from accounts.models import User, Hospital, Staff


class Patient(models.Model):
    basic = models.ForeignKey(User, on_delete=models.CASCADE)
    hospital = models.ManyToManyField(Hospital)

    def __str__(self):
        return User.username


class VitalSign(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    weight = models.SmallIntegerField()
    height = models.SmallIntegerField()
    bmi = models.SmallIntegerField()
    temperature = models.SmallIntegerField()
    systolic_BP = models.CharField(max_length=10)
    diastolic_BP = models.CharField(max_length=10)
    respiratory_rate = models.CharField(max_length=10)
    heart_rate = models.CharField(max_length=10)
    urine_output = models.CharField(max_length=10)
    blood_sugar_R = models.CharField(max_length=10)
    blood_sugar_F = models.CharField(max_length=10)
    taken_by = models.ForeignKey(Staff, on_delete=models.CASCADE)
    taken_at = models.DateTimeField()
    comment = models.TextField()





