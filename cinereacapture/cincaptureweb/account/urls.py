from django.urls import path

from .views import (

    registration_teller, registration_supervisor

)

app_name = 'account'

urlpatterns = [


    path('teller', registration_teller, name="add_teller"),
    path('supervisors', registration_supervisor, name="add_supervisor"),




]
