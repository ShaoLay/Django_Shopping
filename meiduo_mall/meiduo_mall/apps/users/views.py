from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from . import serializers
# Create your views here.


# url(r'^users/$', views.UserView.as_view()),
class UserView(CreateAPIView):
    """
    用户注册

    传入参数：
        username, password, password2, sms_code, mobile, allow
    """
    serializer_class = serializers.CreateUserSerializer


class UsernameCountView(APIView):
    """
    用户名数量
    """
    def get(self,request,username):
        """获取指定用户数量"""
        count = User.objects.filter(username=username).count()

        data = {
            'username':username,
            'count':count
        }

        return Response(data)

class MobileCountView(APIView):
    """手机号数量"""
    def get(self,request,mobile):
        """获取指定手机号数量"""
        count = User.objects.filter(mobile=mobile).count()

        data = {
            'mobile':mobile,
            'count':count
        }

        return Response(data)