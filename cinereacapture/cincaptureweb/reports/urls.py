from django.urls import path

from .views import (


    get_all_service_transaction

)

app_name = 'reports'

urlpatterns = [


    path('sales/all', get_all_service_transaction, name="view_sales"),
    path('expenses/all', get_all_service_transaction, name="expenses"),



]
