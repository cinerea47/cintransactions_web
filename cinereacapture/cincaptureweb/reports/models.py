from django.db import models

from account.models import Account
from .constants import transaction_status, Active, LOGIN_STATUS, LOGGED_IN
from vendor.models import MDevice, ServiceVendor


# Create your models here.

class ServiceTransactions(models.Model):
    user = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL)
    vendor = models.ForeignKey(ServiceVendor, null=True, on_delete=models.SET_NULL)
    device = models.ForeignKey(MDevice, null=True, on_delete=models.SET_NULL)
    amount = models.CharField(max_length=46, unique=False)
    time = models.CharField(max_length=46, unique=False, null=True)
    day = models.CharField(max_length=46, unique=False, null=True)
    transactionID = models.CharField(max_length=46, unique=True)
    type = models.CharField(max_length=46, choices=transaction_status, default=Active)
    description = models.CharField(max_length=46, unique=False)
    status = models.CharField(max_length=46, choices=transaction_status, default=Active)
    transaction_date = models.DateField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self


class ExpenseTransactions(models.Model):
    user = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL)
    device = models.ForeignKey(MDevice, null=True, on_delete=models.SET_NULL)
    amount = models.CharField(max_length=46, unique=False)
    time = models.CharField(max_length=46, unique=False, null=True)
    day = models.CharField(max_length=46, unique=False, null=True)
    sessionID = models.CharField(max_length=46, unique=False, default="0000000")
    transactionID = models.CharField(max_length=46, unique=True)
    description = models.CharField(max_length=46, unique=False)
    status = models.CharField(max_length=46, choices=transaction_status, default=Active)
    transaction_date = models.DateField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self


class Attendance(models.Model):
    user = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL)
    device = models.ForeignKey(MDevice, null=True, on_delete=models.SET_NULL)
    login = models.CharField(max_length=46, unique=False)
    logout = models.CharField(max_length=46, unique=False)
    open_amount = models.IntegerField(max_length=23, unique=False,  default=0)
    closed_amount = models.IntegerField(max_length=23, unique=False, default=0)
    session_id = models.CharField(max_length=46, unique=True)
    date = models.CharField(max_length=46, unique=False, null=True)
    description = models.CharField(max_length=46, unique=False)
    status = models.CharField(max_length=46, choices=LOGIN_STATUS, default=LOGGED_IN)
    date_added = models.DateTimeField(auto_now_add=True)
