from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    role = models.CharField(max_length=50)
    '''is_Hospital_admin = models.BooleanField('Is_hospital_admin', default=False)
    is_Patient = models.BooleanField('Is_Patient', default=False)
    is_Receptionist = models.BooleanField('Is_Receptionist', default=False)
    is_Nurse = models.BooleanField('Is_Nurse', default=False)
    is_Physician = models.BooleanField('Is_Physician', default=False)
    is_Radiologist = models.BooleanField('Is_Radiologist', default=False)
    is_Lab_technician = models.BooleanField('Is_Lab_technician', default=False)
    is_Pharmacy_admin = models.BooleanField('Is_Pharmacy_admin', default=False)
    is_Pharmacist = models.BooleanField('Is_Pharmacist', default=False)'''
    middle_name = models.CharField(max_length=20)
    age = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    zone = models.CharField(max_length=50)
    woreda = models.CharField(max_length=50)
    kebele = models.CharField(max_length=50)
    house_no = models.CharField(max_length=50)
    speciality=models.CharField(max_length=50)

    def __str__(self):
        return self.username