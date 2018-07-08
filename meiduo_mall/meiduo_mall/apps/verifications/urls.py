from django.conf.urls import url

from . import views

urlpatterns = [
url(r'^image_codes/(?P<image_code_id>[\w-]+)/$', views.ImageCodeView.as_view()),
]