from django.db import models

from vendor.constants import(
    ACTIVE_VEN,
    SUSPENDED_VEN,
    VENDOR_STATUS_VEN,
    DEVICE_TYPE_VEN,
    Mobile_ven
)


from account.models import Account


# Create your models here.


class ServiceVendor(models.Model):
    name = models.CharField(max_length=46, unique=False)
    service_name = models.CharField(max_length=46, unique=False)
    code = models.CharField(max_length=46, unique=False)
    description = models.CharField(max_length=46, unique=False)
    status = models.CharField(max_length=46, choices=VENDOR_STATUS_VEN, default=ACTIVE_VEN)
    date_added = models.DateTimeField(auto_now_add=True, null=True)


class MDevice(models.Model):
    city = models.CharField(max_length=46, unique=False)
    branch = models.CharField(max_length=46, unique=False)
    hash_code = models.CharField(max_length=46, unique=False)
    description = models.CharField(max_length=92, unique=False)
    status = models.CharField(max_length=46, choices=VENDOR_STATUS_VEN, default=SUSPENDED_VEN)
    device_name = models.CharField(max_length=92, unique=False, default="unspecified")
    device_number = models.CharField(max_length=92, unique=True, default="0")
    type = models.CharField(max_length=46, choices=DEVICE_TYPE_VEN, default=Mobile_ven)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.ForeignKey(Account, null=True, unique=False, on_delete=models.SET_NULL)
