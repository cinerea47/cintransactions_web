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

from vendor.views import api_activate_device

SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'



# CREATE
@api_view(['POST', ])
# @permission_classes((IsAuthenticated, ))
def activate_device(request):
    if request.method == 'POST':
        new_withdraw = api_activate_device(request)
        response_dic = {"withdraw": new_withdraw}
        print("response_dic", response_dic)
        return JsonResponse(new_withdraw,
                            safe=False, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)
