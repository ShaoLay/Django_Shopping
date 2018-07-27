#!/usr/bin/env python
import sys

sys.path.insert(0, '../')


import os
if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'meiduo_mall.settings.dev'


# 让django初始化
import django
django.setup()

from contents.crons import generate_static_index_html


if __name__ == '__main__':
    generate_static_index_html()