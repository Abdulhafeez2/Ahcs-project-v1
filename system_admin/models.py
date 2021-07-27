from django.db import models

# Create your models here.
from login.models import User


class SystemAdmin:
    basic = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return User.username


class HealthCareProvider(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
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
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    zone = models.CharField(max_length=50)
    woreda = models.CharField(max_length=50)
    kebele = models.CharField(max_length=50)
    dist = models.CharField(max_length=50)

    def __str__(self):
        return self.name
