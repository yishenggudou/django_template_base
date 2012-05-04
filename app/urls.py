#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
    Copyright 2011 timger
    
    +Author timger
    +Gtalk&Email yishenggudou@gmail.com
    +Msn yishenggudou@msn.cn
    +Twitter http://twitter.com/yishenggudou  @yishenggudou
    +Weibo http://t.sina.com/zhanghaibo @timger
    @qiyi
'''


from django.conf.urls.defaults import *
import os
import settings
from django.views.generic.simple import direct_to_template,redirect_to
from views import *
urlpatterns = patterns('',
     (r'^node/(?P<machine_id>.*)/(?P<operate>.*)/(?P<option>.*)/(?P<datatype>.*)$', machine),
     (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': os.path.join(settings.PROJECT_PATH,'static/')}),


)


