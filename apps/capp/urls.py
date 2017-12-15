from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses/$', views.index, name = "capp_index"),
    url(r'^courses/add', views.new, name = "capp_new"),
    url(r'^courses/destroy/(?P<id>\d+)', views.destroy, name = "capp_destroy"),
    url(r'^courses/confirmdestroy/(?P<id>\d+)', views.confdestroy, name = "destroy_conf")
]
