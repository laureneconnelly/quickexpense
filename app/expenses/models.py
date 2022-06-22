from django.db import models

# Create your models here.
class Expense(models.Model):
    date = models.CharField(max_length=70, blank=False, default='')
    amount = models.CharField(max_length=200, blank=False, default='')
    attachment = models.CharField(max_length=70, blank=True, null=True)
    note = models.CharField(max_length=70, blank=True, null=True)
    account_id = models.CharField(max_length=70, blank=False, default='')
    employee_id = models.CharField(max_length=70, blank=False, default='')
    department_id = models.CharField(max_length=70, blank=False, default='')