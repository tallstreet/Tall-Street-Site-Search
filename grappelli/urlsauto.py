# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^settings/', include('grappelli.urls')),
)
