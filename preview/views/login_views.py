# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login as user_login
# restapi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


class LoginView(APIView):

    permission_classes = (permissions.AllowAny,)

    def post(self, request):

        return_data = {
            "msg": "用户名或密码错误！",
            "code": 400,
            "user": {
                "name": "",
            }
        }
        try:
            name = request.data['username']
            password = request.data['password']
            user = authenticate(username=name, password=password)
            if user is None:
                pass
            else:
                user_login(request, user)
                return_data['msg'] = 'success'
                return_data['code'] = 200
                return_data['user']['name'] = user.username
                return_data['user']['user_id'] = user.id
               
        except Exception:
            pass
        response = Response(return_data, status=status.HTTP_200_OK)
        response.set_cookie('name', 'jujule')
        return response
