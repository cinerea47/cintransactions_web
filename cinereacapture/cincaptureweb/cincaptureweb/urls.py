"""
URL configuration for cincaptureweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from personal.views import (
    home_screen_view,
    construction_screen_view,
    forbidden_screen_view,
    update_msg_view,
)

from account.views import (
    registration_view,
    logout_view,
    login_view,
    account_view,
    registration_teller,
    registration_supervisor
)



from vendor.views import(
    get_all_vendors,
    get_all_devices
)
from reports.views import(
    get_all_service_transaction,
    get_all_expenses_transaction,
    get_all_attendance
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # PERSONAL
    path('', home_screen_view, name="home"),
    path('underconstruction/', construction_screen_view, name="construction"),
    path('forbidden/', forbidden_screen_view, name="denied"),
    path('updated/', update_msg_view, name="upadatemsg"),

    # USER ACCOUNT APPS
    path('admin/', admin.site.urls),
    path('register/', registration_view, name="register"),
    path('register/', registration_teller, name="add_teller"),
    path('register/', registration_supervisor, name="add_supervisor"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('account/', account_view, name="account"),
    path('user/', include('account.urls')),
    path('user/api/', include('account.api.urls')),
    # SERVICE VENDOR
    path('vendor/all', get_all_vendors, name="vendors"),
    path('vendor/devices', get_all_devices, name="devices"),
    path('vendor/', include('vendor.urls')),
    path('vendor/api/', include('vendor.api.urls')),#vendor API
    # REPORTS
    path('reports/sales', get_all_service_transaction, name="sales"),
    path('reports/attendance', get_all_attendance, name="attendance"),
    path('reports/expense', get_all_expenses_transaction, name="expenses"),
    path('reports/loans', get_all_service_transaction, name="loans"),
    path('reports/', include('reports.urls')),
    path('reports/api/', include('reports.api.urls')),# REPORTS API


#path('account/', admin.site.urls,"account"),
    #RESET PASSOWRD
    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change'),

    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),

]
