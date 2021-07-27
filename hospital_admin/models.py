from django.db import models

# Create your models here.

from django.db import models


# Create your models here.
from login.models import User


class HospitalAdmin:
    basic = models.OneToOneField(User, on_delete=models.CASCADE)
   # hospital = models.OneToOneField(Hospital, on_delete=models.CASACADE)

    def __str__(self):
        return User.username
