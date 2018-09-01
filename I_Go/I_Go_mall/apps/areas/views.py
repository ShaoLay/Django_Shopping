from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .models import Area
from . import serializers
# Create your views here.


# # GET /areas/
# class AreasView(ListModelMixin, GenericAPIView):
#
#     def list(self):
#
#     def get(self):
#         list()
#
#     查询Area数据 复数
#     序列化返回
#
# class AreasView(ListAPIView):
#
#
# # GET /areas/<pk>/
# class SubAreasView(RetrieveModelMixin, GenericAPIView):
#
#     def retrieve(self):
#
#     def get(self):
#         retrieve()
#
#     查询单一的数据对象
#     序列化返回
#
# class SubAreasView(RetrieveAPIView)


# class AreasViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
class AreasViewSet(CacheResponseMixin, ReadOnlyModelViewSet):

    # 关闭分页处理
    pagination_class = None

    def get_queryset(self):
        if self.action == 'list':
            return Area.objects.filter(parent=None)
        else:
            return Area.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.AreaSerializer
        else:
            return serializers.SubAreaSerializer





# /areas/   {'get': 'list'}  只返回顶级数据  parent=None
# /areas/<pk>  {'get': 'retrieve'}










