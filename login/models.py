from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    role = models.CharField(max_length=50)
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