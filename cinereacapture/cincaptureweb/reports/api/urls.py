from django.urls import path
from reports.api.views import (
    create_service_transaction,
    create_expense_transaction,
    login_attendance,
    re_login_attendance,
    logout_attendance
)

app_name = 'reports'

urlpatterns = [
    # -------------------------reports-------------------------------------
    path('v1/create', create_service_transaction, name="create_transaction"),
    path('v1/expense/create', create_expense_transaction, name="create_expense"),
    path('v1/attendance/login', login_attendance, name="attendance_login"),
    path('v1/attendance/re_login', re_login_attendance, name="attendance_login"),
    path('v1/attendance/logout', logout_attendance, name="attendance_logout"),


]
