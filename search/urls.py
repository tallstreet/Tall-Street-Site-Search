# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('search.views',
    (r'^$', 'index'),
    (r'^search/$', 'search'),
    (r'^update_last_updated/$', 'update_last_updated'),
    (r'^show_id/(?P<key>.+)$', 'show_id'),
    (r'^i18n/', include('django.conf.urls.i18n')),
)
