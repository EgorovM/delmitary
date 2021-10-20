from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    room_number = models.IntegerField()
    telephone = models.CharField(max_length=20)
