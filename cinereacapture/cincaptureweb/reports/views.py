import datetime

from django.db import transaction
from django.db.models import Q
from django.shortcuts import render

from reports.models import (
    ServiceTransactions,
    ExpenseTransactions,
    Attendance
)

from reports.constants import (
    DEPOSIT_REP,
    WITHDRAW_REP,
    TRANSACTION_TYPE_REP,
    BILL_REP
)

from account.models import Account
from vendor.models import ServiceVendor, MDevice

from account.views import get_user_grouptype

from account.settings import get_user_navLinks

from reports.constants import NUMBER_OF_ROWS_PAGE_REP

from reports.constants import LOGGED_IN, LOGGED_OUT


# Create your views here.
def getNumberOfPages(numberOfRows):
    pages = 1
    if numberOfRows != 0:
        if (numberOfRows / NUMBER_OF_ROWS_PAGE_REP) > 0:
            pages = (round(numberOfRows / NUMBER_OF_ROWS_PAGE_REP)) + 1
        else:
            pages = round(numberOfRows / NUMBER_OF_ROWS_PAGE_REP)
    else:
        return 0
    if pages < 1:
        return 1
    else:
        return pages


def getCurrentPage(request, numberOfPages):
    try:
        currentPage = request.GET.get("page")
        return int(currentPage)
    except:
        return 1
    print("currentPage" + currentPage)


def getNextPage(currentPage, numberOfPages):
    nextPage = currentPage + 1
    if nextPage >= numberOfPages:
        return numberOfPages
    else:
        return nextPage


def gePreviousPage(currentPage, numberOfPages):
    prePage = currentPage - 1
    if prePage <= 0:
        return 1
    else:
        return prePage


def getOrderBy(request):
    try:
        order = request.GET.get("sort")
        if order == 'newest':
            return "-transaction_date"
        else:
            return "transaction_date"
    except:
        return "-transaction_date"


def get_attendance_order_By(request):
    try:
        order = request.GET.get("sort")
        if order == 'newest':
            return "-date"
        else:
            return "date"
    except:
        return "-date"


def get_all_service_transaction(request):
    context = {}
    startRow = 0
    servAllTrans = ServiceTransactions.objects.all()
    numberOfPages = getNumberOfPages(len(servAllTrans))
    currentPage = getCurrentPage(request, numberOfPages)
    if request.POST and not request.POST['search'] == '':
        search = (request.POST['search'])
        lookup_search = Q(vendor__service_name__icontains=search) or Q(vendor__name__icontains=search)
        servTrans = ServiceTransactions.objects.filter(lookup_search)
    else:
        if (currentPage == 1):
            startRow = 0
        else:
            startRow = NUMBER_OF_ROWS_PAGE_REP * (currentPage - 1)
        endRow = startRow + NUMBER_OF_ROWS_PAGE_REP
        orderBy = getOrderBy(request)
        servTrans = ServiceTransactions.objects.all().order_by(orderBy)[startRow:endRow]
    context['servTrans'] = servTrans
    context['total_transactions'] = len(servAllTrans)
    context['numberOfPages'] = numberOfPages
    context['currentPage'] = currentPage
    context['nextPage'] = getNextPage(currentPage, numberOfPages)
    context['previousPage'] = gePreviousPage(currentPage, numberOfPages)
    context['rowStartPage'] = startRow
    context['navlinks'] = get_user_navLinks(request)
    return render(request, 'reports/manage_service_transactions.html', context)


def get_all_expenses_transaction(request):
    context = {}
    startRow = 0
    servAllTrans = ExpenseTransactions.objects.all()
    numberOfPages = getNumberOfPages(len(servAllTrans))
    currentPage = getCurrentPage(request, numberOfPages)
    if request.POST and not request.POST['search'] == '':
        search = (request.POST['search'])
        lookup_search = Q(vendor__service_name__icontains=search) or Q(vendor__name__icontains=search)
        servTrans = ServiceTransactions.objects.filter(lookup_search)
    else:
        if (currentPage == 1):
            startRow = 0
        else:
            startRow = NUMBER_OF_ROWS_PAGE_REP * (currentPage - 1)
        endRow = startRow + NUMBER_OF_ROWS_PAGE_REP
        orderBy = getOrderBy(request)
        servTrans = ExpenseTransactions.objects.all().order_by(orderBy)[startRow:endRow]
    context['servTrans'] = servTrans
    context['total_transactions'] = len(servAllTrans)
    context['numberOfPages'] = numberOfPages
    context['currentPage'] = currentPage
    context['nextPage'] = getNextPage(currentPage, numberOfPages)
    context['previousPage'] = gePreviousPage(currentPage, numberOfPages)
    context['rowStartPage'] = startRow
    context['navlinks'] = get_user_navLinks(request)
    return render(request, 'reports/manage_expenses_transactions.html', context)


def get_all_attendance(request):
    context = {}
    startRow = 0
    servAllTrans = Attendance.objects.all()
    numberOfPages = getNumberOfPages(len(servAllTrans))
    currentPage = getCurrentPage(request, numberOfPages)
    if request.POST and not request.POST['search'] == '':
        search = (request.POST['search'])
        lookup_search = Q(vendor__service_name__icontains=search) or Q(vendor__name__icontains=search)
        servTrans = Attendance.objects.filter(lookup_search)
    else:
        if (currentPage == 1):
            startRow = 0
        else:
            startRow = NUMBER_OF_ROWS_PAGE_REP * (currentPage - 1)
        endRow = startRow + NUMBER_OF_ROWS_PAGE_REP
        orderBy = get_attendance_order_By(request)
        servTrans = Attendance.objects.all().order_by(orderBy)[startRow:endRow]
    context['servTrans'] = servTrans
    context['total_transactions'] = len(servAllTrans)
    context['numberOfPages'] = numberOfPages
    context['currentPage'] = currentPage
    context['nextPage'] = getNextPage(currentPage, numberOfPages)
    context['previousPage'] = gePreviousPage(currentPage, numberOfPages)
    context['rowStartPage'] = startRow
    context['navlinks'] = get_user_navLinks(request)
    return render(request, 'reports/manage_attendance_transactions.html', context)


def api_create_service_transaction(request):
    context = {}
    trans_request_status = {'response': "failed"}
    with transaction.atomic():
        user = get_user(int(request.POST['user_uid']))
        vendor = get_vendor(int(request.POST['vendor_uid']))
        m_device = get_device(int(request.POST['device_uid']))
        #m_device = 9
        trans_request_status = get_sales_request_status(vendor, user, m_device)
        if trans_request_status['status'] == 'true':
            service_trans = ServiceTransactions(
                user=user,
                vendor=vendor,
                device=m_device,
                amount=request.POST['amount'],
                time=request.POST['transaction_time'],
                day=request.POST['transaction_day'],
                transactionID=request.POST['transaction_id'],
                type=get_transaction_type(request.POST['type']),
                description=request.POST['description'],
                transaction_date=request.POST['transaction_date']
            )
            service_trans.save()
            trans_request_status['response'] = "created"
        else:
            trans_request_status['response'] = "failed"
    return trans_request_status


def api_create_expense_transaction(request):
    context = {}
    trans_request_status = {'response': "failed"}
    with transaction.atomic():
        user = get_user(int(request.POST['user_uid']))
        m_device = get_device(int(request.POST['device_uid']))
        #m_device = 9
        trans_request_status = get_expense_request_status(user, m_device)
        if trans_request_status['status'] == 'true':
            service_trans = ExpenseTransactions(
                user=user,
                device=m_device,
                amount=request.POST['amount'],
                time=request.POST['transaction_time'],
                day=request.POST['transaction_day'],
                sessionID=request.POST['session_id'],
                transactionID=request.POST['transaction_id'],
                description=request.POST['description'],
                transaction_date=request.POST['transaction_date']
            )
            service_trans.save()
            trans_request_status['response'] = "created"
        else:
            trans_request_status['response'] = "failed"
    return trans_request_status


def get_weekday(day):
    days = [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ]
    try:
        return days[day]
    except:
        return "None"


def get_session_time(user_id):
    ct = datetime.datetime.now()

    print("dateTime: ", ct.second)
    my_date = str(ct.year) + "-" + str(ct.month) + "-" + str(ct.day)
    my_time = str(ct.hour) + ":" + str(ct.minute)
    my_day = get_weekday(ct.weekday())
    print("my_date: ", my_date)
    # ts store timestamp of current time
    ts = ct.timestamp()
    sessiond_id = str(user_id) + str(ts)
    print("sessiond_id: ", sessiond_id)
    return {"session_id": sessiond_id, "date": str(my_date), "time": str(my_time)}


def api_login_attendance(request):
    context = {}
    trans_request_status = {'response': "failed"}
    with transaction.atomic():
        user = get_user(int(request.POST['user_uid']))
        m_device = get_device(int(request.POST['device_uid']))
        amount = get_device(int(request.POST['opening_amount']))
        session_info = get_session_time(user.id)
        enter_attendance(user, m_device, session_info, amount)
        trans_request_status['response'] = "created"
        trans_request_status['session_id'] = session_info["session_id"]
        trans_request_status['sign_in_time'] = session_info["time"]
        trans_request_status['sign_in_date'] = session_info["date"]
    return trans_request_status


def sign_attendance(user_id, device_id, amount):
    context = {}
    trans_request_status = {'response': "failed"}
    with transaction.atomic():
        user = get_user(user_id)
        m_device = get_device(device_id)
        session_info = get_session_time(user.id)
        enter_attendance(user, m_device, session_info, amount)
        trans_request_status['response'] = "created"
        trans_request_status['session_id'] = session_info["session_id"]
        trans_request_status['sign_in_time'] = session_info["time"]
        trans_request_status['sign_in_date'] = session_info["date"]
    return trans_request_status


def loginStatusInfo(user_id):
    context = {}
    trans_request_status = {'response': "failed"}
    with transaction.atomic():
        try:
            attendance = Attendance.objects.get(
                user_id=user_id,
                status=LOGGED_IN
            )
            context["status"] = "true"
            context['sign_in_time'] = attendance.login
            context["sign_in_date"] = attendance.date
            context["session_id"] = attendance.session_id
        except:
            context["status"] = "false"
            context['sign_in_time'] = "-"
            context["sign_in_date"] = "-"
            context["session"] = "-"
        return context


def api_logout_attendance(request):
    context = {}
    trans_request_status = {'response': "failed"}
    with transaction.atomic():
        try:
            attendance = Attendance.objects.get(session_id=request.POST["session_id"])
            session_time = get_session_time(2321)
            attendance.logout = session_time["time"]
            attendance.closed_amount = request.POST["closing_amount"]
            attendance.status = LOGGED_OUT
            attendance.save()
            trans_request_status['response'] = "sign_out"
            trans_request_status['sign_out_time'] = session_time["time"]
            trans_request_status['sign_out_date'] = session_time["date"]
        except:
            pass
    return trans_request_status


def get_transaction_type(transaction_type):
    if transaction_type == DEPOSIT_REP: return DEPOSIT_REP
    if transaction_type == WITHDRAW_REP: return WITHDRAW_REP
    if transaction_type == BILL_REP: return BILL_REP


def enter_attendance(user, m_device, session_info, amount):
    trans_request_status = get_expense_request_status(user, m_device)

    if trans_request_status['status'] == 'true':
        try:
            attendance_report = Attendance(
                user=user,
                device=m_device,
                open_amount=amount,
                #login=request.POST['login_time'],
                login=session_info["time"],
                #date=request.POST['transaction_date'],
                date=session_info["date"],
                #session_id=request.POST['session_id'],
                session_id=session_info["session_id"],
                #description=request.POST['description']
            )
            attendance_report.save()
            return "created"
        except Exception as error_inst:
            print(type(error_inst))  # the exception type
            print(error_inst.args)  # arguments stored in .args
            print(error_inst)
    else:
        return "failed"


def get_user(user_uid):
    user = Account.objects.get(id=user_uid)
    if user is not None:
        return user
    else:
        return None


def get_vendor(vendor_uid):
    vendor = ServiceVendor.objects.get(id=vendor_uid)
    if vendor is not None:
        return vendor
    else:
        return None


def get_device(device_uid):
    device = MDevice.objects.get(id=device_uid)
    if device is not None:
        return device
    else:
        return None


def get_sales_request_status(vendor, user, m_device):
    status = {}
    control = 0
    if vendor is None:
        status['vendor'] = "missing vendor"
        control = 1
    else:
        status['vendor'] = "present"
    if user is None:
        status['user'] = "missing user"
        control = 1
    else:
        status['user'] = "present"
    if m_device is None:
        status['m_device'] = "missing"
        control = 1
    else:
        status['m_device'] = "present"
    if control == 0:
        status['status'] = "true"
    else:
        status['status'] = "None"
    return status


def get_expense_request_status(user, m_device):
    status = {}
    control = 0
    if user is None:
        status['user'] = "missing user"
        control = 1
    else:
        status['user'] = "present"
    if m_device is None:
        status['m_device'] = "missing"
        control = 1
    else:
        status['m_device'] = "present"
    if control == 0:
        status['status'] = "true"
    else:
        status['status'] = "None"
    return status
