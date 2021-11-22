from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.utils import timezone


class Department(models.Model):
    objects = models.Manager()
    department_name = models.CharField(max_length=20)
    department_description = models.CharField(max_length=50)


class PayGrade(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=20, default=None)
    base_pay = models.IntegerField()
    house_rent_allowance = models.IntegerField()
    dearness_allowance = models.IntegerField()
    bonus = models.FloatField()


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
    age = models.IntegerField(null=True)
    role = models.CharField(choices=roles, max_length=10)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    pay_grade = models.ForeignKey(PayGrade, on_delete=models.SET_NULL, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.username
