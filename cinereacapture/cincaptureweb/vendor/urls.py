from django.urls import path

from .views import (

    get_all_devices,
    create_app_device,
    device_view_activation,
    get_all_vendors,
    create_vendor

)

app_name = 'vendor'

urlpatterns = [

    path('device/create', create_app_device, name="create_device"),
    path('device/all', get_all_devices, name="devices"),
    path('device/activate', device_view_activation, name="view_devices"),
    path('create', create_vendor, name="create_vendor"),
    path('all', get_all_vendors, name="vendor"),



]
