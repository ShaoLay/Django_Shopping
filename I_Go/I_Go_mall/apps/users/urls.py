from django.conf.urls import url
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from . import views


urlpatterns = [
    url(r'^users/$', views.UserView.as_view()),
    url(r'^usernames/(?P<username>\w{5,20})/count/$', views.UsernameCountView.as_view()),
    url(r'^mobiles/(?P<mobile>1[3-9]\d{9})/count/$', views.MobileCountView.as_view()),
    # url(r'^authorizations/$', obtain_jwt_token),  # 登录认证
    url(r'^authorizations/$', views.UserAuthorizeView.as_view()),  # 登录认证, 补充了合并购物车
    url(r'^user/$', views.UserDetailView.as_view()),  # 个人中心基本信息
    url(r'^email/$', views.EmailView.as_view()),
    url(r'^emails/verification/$', views.VerifyEmailView.as_view()),
    url(r'^browse_histories/$', views.UserBrowsingHistoryView.as_view()),
]

router = routers.DefaultRouter()
router.register(r'addresses', views.AddressViewSet, base_name='addresses')

urlpatterns += router.urls