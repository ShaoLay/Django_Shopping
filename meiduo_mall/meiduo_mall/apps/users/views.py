from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from . import serializers


# Create your views here.

class UserView(CreateAPIView):
    """
    用户注册
    传入参数：
        username,password,password2,sms_code,mobile,allow
    """
    serializers_class = serializers.CreateUserSerializer