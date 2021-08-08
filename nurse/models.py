from django.db import models

# Create your models here.
from accounts.models import User, Hospital


class Nurse(models.Model):
    basic = models.ForeignKey(User, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return User.username
