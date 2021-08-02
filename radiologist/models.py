from django.db import models

# Create your models here.
from accounts.models import User


class Radiologist:
    basic = models.OneToOneField(User, on_delete=models.CASCADE)
    #hospital = models.ManyToOneRel(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return User.username
