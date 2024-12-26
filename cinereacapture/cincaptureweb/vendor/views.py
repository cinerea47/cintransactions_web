from django.db import transaction
from django.db.models import Q, Max
from django.http import HttpResponseRedirect
from django.shortcuts import render

from vendor.constants import (
    DEVICE_TYPE_VEN,
    ACTIVE_VEN
)
from vendor.forms import MDeviceForm, ServiceVendorForm
from vendor.models import MDevice, ServiceVendor

from vendor.DeviceAuthenticationManager import DeviceAuthenticationManager

from account.settings import get_user_navLinks


# Create your views here.
def get_all_devices(request):
    context = {}
    if request.POST and not request.POST['search'] == '':
        search = (request.POST['search'])
        lookup_search = Q(title_icontains=search)
        device = MDevice.objects.filter(lookup_search)
    else:
        device = MDevice.objects.all()
    context['devices'] = device
    context['total_devices'] = len(device)
    context['page_navbar'] = "SET_OFF_PER"
    context['navlinks'] = get_user_navLinks(request)
    return render(request, 'vendor/manage_devices.html', context)


def create_app_device(request):
    context = {}
    if request.POST:
        form = MDeviceForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                device_info_inst = form.save()
                print("form Saved")
                authen_device = DeviceAuthenticationManager()
                device_pin_hash = authen_device.generate_pin_hash()
                MDevice.objects.filter(pk=device_info_inst.id).update(
                    device_number=generate_device_number(),
                    hash_code=device_pin_hash['hash']
                )
                pin = device_pin_hash['pin']
                return HttpResponseRedirect(
                    '/vendor/device/activate?device=' + str(device_info_inst.id) + '&pin=' + pin)

        context['FormResponse'] = form(request.POST)
        context['DeviceRegisterForm'] = form
        print("Not Post Request")
    context['DeviceRegisterForm'] = MDeviceForm()
    context['device_types'] = DEVICE_TYPE_VEN
    context['navlinks'] = get_user_navLinks(request)
    return render(request, 'vendor/create_app_device.html', context)


def device_view_activation(request):
    context = {}
    device = MDevice.objects.get(id=request.GET.get("device"))
    context['device'] = device
    context['activation_code'] = request.GET.get("pin")
    return render(request, 'vendor/view_activation.html', context)


def get_all_vendors(request):
    context = {}
    if request.POST and not request.POST['search'] == '':
        search = (request.POST['search'])
        lookup_search = Q(title_icontains=search)
        vendors = ServiceVendor.objects.filter(lookup_search)
    else:
        vendors = ServiceVendor.objects.all()
    context['vendors'] = vendors
    context['total_vendors'] = len(vendors)
    context['page_navbar'] = "SET_OFF_PER"
    context['navlinks'] = get_user_navLinks(request)
    return render(request, 'vendor/manage_vendors.html', context)


def create_vendor(request):
    context = {}
    if request.POST:
        form = ServiceVendorForm(request.POST)
        if form.is_valid():
            vendor_info_inst = form.save()
            print("form Saved")
            return HttpResponseRedirect('/vendor/all')

        context['FormResponse'] = form(request.POST)
        context['ServiceVendorForm'] = form
        print("Not Post Request")
    context['ServiceVendorForm'] = ServiceVendorForm()
    context['navlinks'] = get_user_navLinks(request)
    return render(request, 'vendor/create_vendor.html', context)


# =============================
def generate_device_number():
    current_pin = MDevice.objects.aggregate(Max('device_number'))
    #args = DeviceFirstRunActivation.objects.all()  # or whatever arbitrary queryset
    #args.aggregate(Max('activation_request_pin'))

    if current_pin['device_number__max'] is None:
        return 100191
    current_pin_int = int(current_pin['device_number__max'])
    if current_pin_int >= 100191:
        new_account = current_pin_int + 1
    else:
        new_account = 100191
    return new_account


# ================================= API =======================================

def api_activate_device(request):
    with transaction.atomic():
        check_device = MDevice.objects.filter(device_number=request.POST['mdevice_code'])
        if len(check_device) > 0:
            device = MDevice.objects.get(device_number=request.POST['mdevice_code'])
            authen_device = DeviceAuthenticationManager()
            if authen_device.verify_activation_code(device, request.POST['activation_code']):
                device.status = ACTIVE_VEN
                device.device_name = request.POST['device_name']
                device.save()
            return {
                'response': "success",
                'status': 'success',
                'message': 'device_activate',
                'value': "1"
            }
    return {
        'response': "failed",
        'status': 'None',
        'message': 'None',
        'value': "0"
    }
