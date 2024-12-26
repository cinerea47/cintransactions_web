
from account.constants import TELLER_ACC, SUPERVISOR_ACC

linkhome = 'home'
linkadd_teller = 'add_teller'
linkadd_supervisor = 'add_supervisor'
linksales = 'sales'
linkexpense= 'expense'
linkattendance = 'attendance'
linkloans = 'loans'
linkvendor = 'vendor'
linkdevice = 'device'


links = [
    (linkhome, 'home'),
    (linkadd_teller, 'add_teller'),
    (linkadd_supervisor,'add_supervisor'),
    (linksales, 'sales'),
    (linkexpense, 'expense'),
    (linkattendance, 'attendance'),
    (linkloans, 'loans'),
    (linkvendor, 'vendor'),
    (linkdevice,'device'),

]

#ALLOWED USER LINKS: ADD OR REMOVE FROM LIST
def get_user_navLinks(request):
    if request.user.is_authenticated:
        if request.user.usergrouptypes.lower() == TELLER_ACC.lower():
            return [linkhome, linkadd_teller]
        elif request.user.usergrouptypes.lower() == SUPERVISOR_ACC.lower():
            return [
                linkhome,linksales, linkexpense, linkattendance, linkloans,
                linkadd_teller, linkadd_supervisor, linkvendor, linkdevice
            ]
        else:
            return [linkhome]
    else:
        return [linkhome]