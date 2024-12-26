from django.urls import path

from vendor.api.views import(
    activate_device
)

app_name = 'vendor'

urlpatterns = [
    # -------------------------Reports-------------------------------------
    path('device/activate', activate_device, name="activation"),

]
