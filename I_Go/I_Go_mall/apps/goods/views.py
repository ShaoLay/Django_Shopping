from django.shortcuts import render
from drf_haystack.viewsets import HaystackViewSet
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView

from .serializers import SKUSerializer, SKUIndexSerializer
from .models import SKU
# Create your views here.


# /categories/(?P<category_id>\d+)/skus?page=xxx&page_size=xxx&ordering=xxx
class SKUListView(ListAPIView):
    """
    商品列表视图
    """
    serializer_class = SKUSerializer
    # queryset = SKU.objects.filter(category=???)

    # 排序
    filter_backends = [OrderingFilter]
    ordering_fields = ('create_time', 'price', 'sales')

    # 分页, 全局设置

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return SKU.objects.filter(category_id=category_id, is_launched=True)


class SKUSearchViewSet(HaystackViewSet):
    """
    SKU搜索
    """
    index_models = [SKU]

    serializer_class = SKUIndexSerializer