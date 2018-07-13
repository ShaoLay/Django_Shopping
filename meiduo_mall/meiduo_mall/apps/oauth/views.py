from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import OAuthQQ
from .exceptions import OAuthQQAPIError


# Create your views here.


#  url(r'^qq/authorization/$', views.QQAuthURLView.as_view()),
class QQAuthURLView(APIView):
    """
    获取QQ登录的url    ?next=xxx
    """
    def get(self, request):
        # 获取next参数
        next = request.query_params.get("next")

        # 拼接QQ登录的网址
        oauth_qq = OAuthQQ(state=next)
        login_url = oauth_qq.get_login_url()

        # 返回
        return Response({'login_url': login_url})


class QQAuthUserView(APIView):
    """
    QQ登录的用户  ?code=xxxx
    """
    def get(self, request):
        # 获取code
        code = request.query_params.get('code')

        if not code:
            return Response({'message': '缺少code'}, status=status.HTTP_400_BAD_REQUEST)

        # 凭借code 获取access_token
        oauth_qq = OAuthQQ()
        try:
            access_token = oauth_qq.get_access_token(code)
        except OAuthQQAPIError:
            return Response({'message': '获取access_token失败'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        # 凭借access_token获取 openid

        # 根据openid查询数据库OAuthQQUser  判断数据是否存在

        # 如果数据存在，表示用户已经绑定过身份， 签发JWT token

        # 如果数据不存在，处理openid 并返回























