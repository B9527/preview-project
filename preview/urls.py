#!/usr/bin/python
# coding:utf-8

from django.conf.urls import url
from preview.views.login_views import LoginView
from preview.views import config_views


urlpatterns = [
    url(r'^login/$', LoginView.as_view()),
    url(r'^config/upload/$', config_views.UploadSettingViews.as_view()),
    url(r'^config/input/$', config_views.InputSettingViews.as_view()),
    url(r'^config/list/$', config_views.PreviewConfigListViews.as_view()),
    url(r'^table/$', config_views.PreviewTableFieldsViews.as_view()),
    url(r'^table/data/$', config_views.PreviewTableDataViews.as_view()),
]