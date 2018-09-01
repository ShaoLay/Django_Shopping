from haystack import indexes

from .models import SKU


class SKUIndex(indexes.SearchIndex, indexes.Indexable):
    # 作用
    # 1. 明确在搜索引擎中索引数据包含哪些字段
    # 2. 字段也会作为前端进行检索查询时关键词的参数名

    text = indexes.CharField(document=True, use_template=True)

    id = indexes.IntegerField(model_attr='id')
    name = indexes.CharField(model_attr='name')
    price = indexes.DecimalField(model_attr='price')
    default_image_url = indexes.CharField(model_attr='default_image_url')
    comments = indexes.IntegerField(model_attr='comments')

    def get_model(self):
        # 指明使用的数据库
        return SKU

    def index_queryset(self, using=None):
        # 指明数据库数据建立索引的范围
        # return SKU.objects.filter(is_launched=True)
        return self.get_model().objects.filter(is_launched=True)

# ?text=iphone
# ?id=
# ?name=