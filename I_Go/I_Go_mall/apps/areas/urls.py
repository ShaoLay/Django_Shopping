from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views


urlpatterns = [
]

router = DefaultRouter()
router.register('areas', views.AreasViewSet, base_name='areas')

urlpatterns += router.urls


# /areas/   {'get': 'list'}  只返回顶级数据  parent=None  name=xx
# /areas/<pk>  {'get': 'retrieve'}  name=xxx