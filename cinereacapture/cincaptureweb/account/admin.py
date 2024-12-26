from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
from account.models import Account


class AccountAdmin( admin.ModelAdmin):
    list_display = ('email','username', 'firstname', 'lastname', 'date_joined', 'last_login', 'is_admin','is_staff')
    search_fields = ('email','username', 'firstname','lastname')
    readonly_fields=('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()



admin.site.register(Account, AccountAdmin)


# Register your models here.
