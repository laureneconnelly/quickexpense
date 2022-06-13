from django.db import models

# Create your models here.
class Employee(models.Model):
    username = models.CharField(max_length=70, blank=False, default='')
    password = models.CharField(max_length=200, blank=False, default='')
    charge_type = models.CharField(max_length=70, blank=True, null=True)
