from django.db import models

# Create your models here.
class Account(models.Model):
    account_no = models.CharField(max_length=70, blank=False, default='')
    account_name = models.CharField(max_length=200, blank=False, default='')