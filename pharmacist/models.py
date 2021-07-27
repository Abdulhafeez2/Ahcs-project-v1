from django.db import models

# Create your models here.
from login.models import User


class Pharmacist:
    basic = models.OneToOneField(User, on_delete=models.CASCADE)
    #pharmacy = models.ManyToOneRel(Pharmacy, on_delete=models.CASCADE)

    def __str__(self):
        return User.username
