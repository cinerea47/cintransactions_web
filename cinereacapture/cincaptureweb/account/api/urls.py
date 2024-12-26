from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from account.api.views import(
    CustomAuthToken,
)

app_name = 'account'

urlpatterns = [
    path('login2', obtain_auth_token, name="login"), # -> see accounts/api/views.py for response and url info
    path('v1/login', CustomAuthToken.as_view(), name="login") # -> see accounts/api/views.py for response and url info

]
