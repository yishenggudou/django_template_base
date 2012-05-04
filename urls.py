from django.conf.urls.defaults import *
import os
import settings
from django.views.generic.simple import direct_to_template,redirect_to

urlpatterns = patterns('',

     
     
     (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': os.path.join(settings.PROJECT_PATH,'static/')}),


)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

#https://docs.djangoproject.com/en/dev/howto/static-files/
