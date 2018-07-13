from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^users/$',views.UserView.as_view()),
]