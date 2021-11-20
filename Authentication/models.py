from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
from django.utils import timezone


class User(AbstractUser):
    roles = [
        ('ENG', 'Engineer'),
        ('DES', 'Designer'),
        ('MAG', 'Manager'),
        ('SCI', 'Researcher'),
        ('FIN', 'Finance'),
        ('HR', 'HR')
    ]
    mobile = models.CharField(max_length=10)
    age = models.IntegerField(max_length=70)
    role = models.CharField(choices=roles, max_length=10)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username
