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
PROJECT_PATH = os.path.split(os.path.abspath(__file__))[0]
PROJECT_DIR , PROJECT_ROOT = PROJECT_PATH, PROJECT_PATH
PROJECT_NAME = PROJECT_PATH.strip().strip('/').split('/')[-1]

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
DATABASE_ENGINE = ''           # 'postg
DATABASE_NAME = ''             # Or 
DATABASE_USER = ''             # Not
DATABASE_PASSWORD = ''         # Not
DATABASE_HOST = ''  
DATABASE_PORT = ''             # Set to 

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

LOGFILE = os.path.join(PROJECT_DIR,PROJECT_NAME+'.log')

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"


MEDIA_ROOT = os.path.join(PROJECT_ROOT,'media')
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

MEDIA_URL = '/media/'

# user {{ STATIC_URL }} in template
STATIC_URL = "/static/"

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'q_*@d(@rqa+a=7n%sgfu)_9%4zj_(41b!xspaj+j9d(bk6@ytu'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',

#    'django.template.loaders.filesystem.Loader',
#    'django.template.loaders.app_directories.Loader',
#    'django.template.loaders.eggs.Loader',
)


TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR,'templates'),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'app.Middleware.Middleware',
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = PROJECT_NAME+'.urls'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    #'django.contrib.messages',
    # Uncomment the next line to enable the admin:
     'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
     'django.contrib.admindocs',
)

#https://docs.djangoproject.com/en/dev/topics/http/views/
handler500 = 'mysite.views.my_custom_error_view'
handler404 = 'mysite.views.my_custom_404_view'
handler403 = 'mysite.views.my_custom_permission_denied_view'


################# for web app #################################
LOGIN_URI = '/login/'
LOGOUT_URI = '/logout/'
REGISTION_URI = '/registion/'
SQLURI = "mysql://user:password@host:port/database?charset=utf8"

#from sqlalchemy import Table, create_engine, MetaData, and_, or_, desc
#engine = create_engine(SQLURI, echo=True,echo_pool=True,pool_recycle=720)
#metadata = MetaData(engine)
#S3_USER = Table('s3_user',metadata,autoload=True)


