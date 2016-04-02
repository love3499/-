#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import patterns, include, url
from django.conf import settings
urlpatterns = patterns('',
    url(r'^$', 'showImg.views.show'),
    url( r'^media/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root':settings.MEDIA_ROOT }),
)

