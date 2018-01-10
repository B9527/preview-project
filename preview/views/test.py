# coding:utf-8

from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import ObtainJSONWebToken


class CookieJSONWebToken(ObtainJSONWebToken):
    """
    接受post请求生成JWT-Token并设置cookie
    """

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            response_data = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER(
                token, user, request)
            res = Response(response_data)
            res.set_cookie(api_settings.JWT_AUTH_HEADER_PREFIX.upper(), value=response_data[
                           'token'], httponly=True, expires=datetime.now() + api_settings.JWT_EXPIRATION_DELTA)
            return res
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)