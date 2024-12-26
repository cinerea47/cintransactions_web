from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import JsonResponse
from django.db.models import Q
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView

from account.models import Account

from reports.views import (
    api_create_service_transaction,
    api_create_expense_transaction,
    api_login_attendance,
    api_logout_attendance
)

SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'


# CREATE SALES
#@api_view(['POST', ])
# @permission_classes((IsAuthenticated, ))
def create_service_transaction(request):
    if request.method == 'POST':
        new_transaction = api_create_service_transaction(request)
        response_dic = {"withdraw": new_transaction}
        print("response_dic", response_dic)
        return JsonResponse(new_transaction,
                            safe=False, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)


# CREATE EXPENSES
#@api_view(['POST', ])
# @permission_classes((IsAuthenticated, ))
def create_expense_transaction(request):
    if request.method == 'POST':
        new_transaction = api_create_expense_transaction(request)
        response_dic = {"withdraw": new_transaction}
        print("response_dic", response_dic)
        return JsonResponse(new_transaction,
                            safe=False, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)


#@api_view(['POST', ])
# @permission_classes((IsAuthenticated, ))
def login_attendance(request):
    if request.method == 'POST':
        new_attendance = api_login_attendance(request)
        response_dic = {"attendance": new_attendance}
        print("response_dic", response_dic)
        return JsonResponse(new_attendance,
                            safe=False, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)


def re_login_attendance(request):
    if request.method == 'POST':
        new_attendance = api_login_attendance(request)
        response_dic = {"attendance": new_attendance}
        print("response_dic", response_dic)
        return JsonResponse(new_attendance,
                            safe=False, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)


#@api_view(['POST', ])
# @permission_classes((IsAuthenticated, ))
def logout_attendance(request):
    if request.method == 'POST':
        new_attendance = api_logout_attendance(request)
        response_dic = {"attendance": new_attendance}
        print("response_dic", response_dic)
        return JsonResponse(new_attendance,
                            safe=False, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)
