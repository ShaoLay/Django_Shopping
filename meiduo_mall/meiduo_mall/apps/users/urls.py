from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from . import views


urlpatterns = [
    url(r'^users/$',views.UserView.as_view()),
    url(r'^authorizations/$', obtain_jwt_token),  # 登录认证
]