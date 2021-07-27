from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Address(models.Model):
    region = models.CharField(max_length=50)
    zone = models.CharField(max_length=50)
    woreda = models.CharField(max_length=50)
    kebele = models.CharField(max_length=50)
    house_no = models.CharField(max_length=50)

    def __str__(self):
        return self.wereda

