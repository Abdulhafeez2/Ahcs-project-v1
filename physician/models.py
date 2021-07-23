from django.db import models
from login.models import User
# Create your models here.
class patient_waiting_list(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    receptionist=models.BooleanField(default=False)
    nurse=models.BooleanField(default=False)
    triage=models.BooleanField(default=False)
    physician=models.BooleanField(default=False)
    radiologist=models.BooleanField(default=False)
    lab_technician=models.BooleanField(default=False)
    department=models.CharField(max_length=25)

