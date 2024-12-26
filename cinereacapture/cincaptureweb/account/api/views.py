from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from reports.views import sign_attendance, loginStatusInfo

from account.constants import INITIATED_LOGIN, CONTINUED_LOGIN


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        device_id = request.POST["device_uid"]
        amount = request.POST["opening_amount"]
        logStatusInfo = loginStatusInfo(user.pk)
        isLogged_in = logStatusInfo["status"]
        if isLogged_in == "false":
            session_info = sign_attendance(user.pk, device_id, amount)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.email,
                'username': user.username,
                'firstname': user.firstname,
                'lastname': user.lastname,
                'session': session_info["session_id"],
                "sign_in_time": session_info['sign_in_time'],
                "sign_in_date": session_info["sign_in_date"],
                "status": INITIATED_LOGIN,
            })
        else:
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.email,
                'username': user.username,
                'firstname': user.firstname,
                'lastname': user.lastname,
                'session': logStatusInfo["session_id"],
                "sign_in_time": logStatusInfo['sign_in_time'],
                "sign_in_date": logStatusInfo["sign_in_date"],
                "status": CONTINUED_LOGIN,
            })
