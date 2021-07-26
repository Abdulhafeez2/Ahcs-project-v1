from django.db import models


# Create your models here.
from login.models import User


class HealthCareProvider(models.Model):
    #admin = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    zone = models.CharField(max_length=50)
    woreda = models.CharField(max_length=50)
    kebele = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pharmacy(models.Model):
    #admin = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    zone = models.CharField(max_length=50)
    woreda = models.CharField(max_length=50)
    kebele = models.CharField(max_length=50)

    def __str__(self):
        return self.name
