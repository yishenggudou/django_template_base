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

import os
import sys
import urlparse
from django.http import HttpResponse
try:
    import json
except:
    from django.utils import simplejson as json

__author__ = 'timger & yishenggudou@gmail.com'
__license__ = '@qiyi'
__version__ = (0,0,0)



class  Middleware(object):
    u"""
    Django Middleware class for amazon s3 REST Authorization API
    """
    
    def process_request(self, request):
        u"""
        -------------------------------------------------------------------
            check Bucket Acl
        -------------------------------------------------------------------
        """
        
        #### django META中会加上HTTP_ 并且将-替换为_ 
        headers = dict([(str(i[0].replace('HTTP_','').upper()),i[1]) for i in request.META.items() if i[0].startswith('HTTP_')])
        headers_from_get = dict([(str(i[0]).upper(),(isinstance(i[1],list) and str(i[1][0])) or (isinstance(i[1],unicode)) and i[1].encode('utf-8')) for i in request.GET.items()])
        headers.update(headers_from_get)
        ####read header args from post or get payload json data
        if request.GET.get('payload') :
            #try:
                headers_from_json = json.loads(request.GET.get('payload')).get('headers')
                headers.update(headers_from_json)
            #except:
            #    pass
        if request.POST.get('payload') :
	    
            try:
                headers_from_json = json.loads(request.POST.get('payload')).get('headers')
                print headers_from_json
                headers.update(headers_from_json)
            except:
                pass

        del headers['HOST']
        request.uheaders  = dict([(str(i[0]).upper(),(isinstance(i[1],str) and str(i[1])) or (isinstance(i[1],unicode)) and i[1].encode('utf-8')) for i in headers.items()])
        print headers


