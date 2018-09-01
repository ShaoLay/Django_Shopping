from celery_tasks.main import celery_app
from django.template import loader
from django.conf import settings
import os

from goods.utils import get_categories
from goods.models import SKU


@celery_app.task(name='generate_static_sku_detail_html')
def generate_static_sku_detail_html(sku_id):
    """
    生成静态商品详情页面
    :param sku_id: 商品sku id
    """
    # 商品分类菜单
    categories = get_categories()

    # 获取当前sku的信息
    sku = SKU.objects.get(id=sku_id)   # 华为手机对象
    sku.images = sku.skuimage_set.all()

    # 面包屑导航信息中的频道
    goods = sku.goods
    goods.channel = goods.category1.goodschannel_set.all()[0]

    sku_specs = sku.skuspecification_set.order_by('spec_id')

    sku_key = []
    for spec in sku_specs:
        sku_key.append(spec.option.id)


    # 获取当前商品的所有SKU
    skus = goods.sku_set.all()
    spec_sku_map = {}
    # skus = [{华为手机sku对象},{},{}]
    for s in skus:
        # s {华为手机sku对象}
        # 获取sku的规格参数
        s_specs = s.skuspecification_set.order_by('spec_id')
        # s_specs =[{spec_id: 6 颜色, option: 14 蓝色}, {spec_id: 7 版本, options: 21 128G}]
        # 用于形成规格参数-sku字典的键
        key = []
        for spec in s_specs:
            key.append(spec.option.id)
        # key = [14, 21]
        # 向规格参数-sku字典添加记录
        spec_sku_map[tuple(key)] = s.id

    # 获取当前商品的规格信息
    #specs = [
    #    {
    #        'name': '屏幕尺寸',
    #        'options': [
    #            {'value': '13.3寸', 'sku_id': xxx},
    #            {'value': '15.4寸', 'sku_id': xxx},
    #        ]
    #    },
    #    {
    #        'name': '颜色',
    #        'options': [
    #            {'value': '银色', 'sku_id': xxx},
    #            {'value': '黑色', 'sku_id': xxx}
    #        ]
    #    },
    #    ...
    #]
    specs = goods.goodsspecification_set.order_by('id')
    # specs = [{name: 颜色}, {name: 版本}]
    # 若当前sku的规格信息不完整，则不再继续
    if len(sku_key) < len(specs):
        return
    for index, spec in enumerate(specs):

        # index=0 spec = {name: 颜色},


        # 复制当前sku的规格键
        # sku_key = [13, 20]
        key = sku_key[:]
        # key = [13, 20]

        # 该规格的选项
        options = spec.specificationoption_set.all()
        # options = [{value: 蓝 id 14}, {value: 金  id 13},  {value： 红 id 15}]
        for option in options:
            # option = {value: 蓝 id 14}
            # 在规格参数sku字典中查找符合当前规格的sku
            key[index] = option.id  # -> [14, 20]

            # spec_sku_map = {
            #       (颜色， 版本)
            #      (13, 20): 9,
            #      (13, 21): 12,
            #      (14, 20): 13
            # }
            option.sku_id = spec_sku_map.get(tuple(key))
            # option {value: 蓝 id 14, sku_id:13}

        spec.options = options
        # spec = {name: 颜色, options:[{value: 金  id 13}, {value: 蓝 id 14}, {value： 红 id 15}] }

    # 渲染模板，生成静态html文件
    context = {
        'categories': categories,
        'goods': goods,  # SPU
        'specs': specs,  # 规格
        'sku': sku
    }

    template = loader.get_template('detail.html')
    html_text = template.render(context)
    file_path = os.path.join(settings.GENERATED_STATIC_HTML_FILES_DIR, 'goods/'+str(sku_id)+'.html')

    # /front_end_pc/goods/1.html  2.html

    with open(file_path, 'w') as f:
        f.write(html_text)








