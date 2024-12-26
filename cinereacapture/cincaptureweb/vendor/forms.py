from django import forms

from .models import (
    ServiceVendor,
    MDevice
)


class ServiceVendorForm(forms.ModelForm):
    list_display = ("name", "service_name", "description")

    class Meta:
        model = ServiceVendor
        fields = ("name", "service_name", "description")


class MDeviceForm(forms.ModelForm):
    list_display = ("city", "branch", "description", "type")

    class Meta:
        model = MDevice
        fields = ("city", "branch", "description", "type")
