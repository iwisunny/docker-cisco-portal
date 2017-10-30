# Django settings for mysite project.
import os

DEBUG = True
ALLOWED_HOSTS = ['*']
TEMPLATE_DEBUG = DEBUG
BASE = "/pitrix/lib/pitrix-websupervisor"

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': '', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Harbin'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
gettext = lambda s: s
LANGUAGE_COOKIE_NAME = 'lang'
LANGUAGE_CODE = 'zh-cn'
LANGUAGES = (
    ('en', gettext('English')),
    ('zh-cn', gettext('Chineses Simplified')),
)

LOCALE_PATHS = (os.path.join(BASE, 'locale'),)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/pitrix/lib/pitrix-websupervisor/static',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ys2@7co7g56+(gbg5qc9etoc5i83zpnr=6o53_at35kb!%6elf'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'mysite.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #os.path.join(os.path.dirname(BASE), 'templates'),
    "/pitrix/lib/pitrix-websupervisor/templates",
)

INSTALLED_APPS = (
    'mysite.apps.custom_ext',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'coffin',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# CACHE BACKEND
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# SESSION
SESSION_COOKIE_NAME = "sid"
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7

# Using Memcache as session storage backend
#SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
# Using File as session storage backend
SESSION_ENGINE = 'django.contrib.sessions.backends.file'
SESSION_FILE_PATH = '/tmp'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


JINJA2_ENVIRONMENT_OPTIONS = {
        'cache_size': 0 if DEBUG else 50,
        }

# pitrix constants
PITRIX_SETTINGS = {
        # download file root
        'download_root': "/pitrix/lib/pitrix-websupervisor/storage",
        # static file root
        'static_file_root': "/pitrix/lib/pitrix-websupervisor/static",
        # biz team's namelist
        'biz_team_namelist': "online",
        # restrict admin requests in this server port, if port is "", all admin requests is allowed
        'admin_server_port': "8081",
        # auto version will turned on if True and close if False
        'auto_version': False,
        # enable signup function
        'enable_signup': True,
        # public zones that can be access by newly registered user
        'public_zones': ["beta"],
        'api_server': {
            'host': '192.168.5.3',
            'port': 7777,
            'protocol': 'http',
            'session_uri': '/i2/',
            'console_uri': '/i3/',
            'msg_time_out':10,
            'http_socket_timeout':15,
            # here is your console key
            'console_key_id':'DIHCTODNZBSSPKDGTOHO',
            'console_secrect_key':'EGcAuqxv6jO32hO3mDrEx2uTzRuUNl5T6v5zfHsf',
        },
        # stark allinone
        # 'api_server': {
        #   'host': '172.31.8.32',
        #   'port': 8882,
        #   'protocol': 'http',
        #   'session_uri': '/i2/',
        #   'sessoin_uri': '/i2/',
        #   'console_uri': '/i3/',
        #   'msg_time_out':10,
        #   'http_socket_timeout':15,
        #   # here is your console key
        #   'console_key_id':'XYIYJEMMSPVUBVWUEARY',
        #   'console_secrect_key':'8qyMBHGHilfoDc1c89NqrMjsFF7S9Q6FkRhtEfpR',
        # },
        # qingstor server
        'qs_config': {
            'qy_access_key_id': 'AZEUHKROAGGAZSDMSCIQ',
            'qy_secret_access_key': '6wnVEWHPXq02EpVSNd9mzaKnZgLAzxV6OuzRMKcQ',
            'endpoint': 'qingstorage.com',
            'port': '80',
            # 'proxy': ['proxy0:8981'],
            'protocol': 'http',
            'verify_ssl': True,
            'maxFileNum': 10,
            'chunkSize': 64*1024*1024,
            'maxFileSize': 1024*1024*1024,
            #'customed_endpoints': {
            #  'zw': 'zw.qingstorage.com'
            #}
        }
}

SITE_URL = 'https://www.qingcloud.com'
PUSH_URL = 'https://console.staging.com'
DOCS_URL = 'https://docs.qingcloud.com'

# ===============================================================================
# http://modwsgi.readthedocs.io/en/develop/user-guides/reloading-source-code.html

import os
import sys
import time
import signal
import threading
import atexit
import Queue

_interval = 1.0
_times = {}
_files = []

_running = False
_queue = Queue.Queue()
_lock = threading.Lock()

def _restart(path):
    _queue.put(True)
    prefix = 'monitor (pid=%d):' % os.getpid()
    print >> sys.stderr, '%s Change detected to \'%s\'.' % (prefix, path)
    print >> sys.stderr, '%s Triggering process restart.' % prefix
    os.kill(os.getpid(), signal.SIGINT)

def _modified(path):
    try:
        # If path doesn't denote a file and were previously
        # tracking it, then it has been removed or the file type
        # has changed so force a restart. If not previously
        # tracking the file then we can ignore it as probably
        # pseudo reference such as when file extracted from a
        # collection of modules contained in a zip file.

        if not os.path.isfile(path):
            return path in _times

        # Check for when file last modified.

        mtime = os.stat(path).st_mtime
        if path not in _times:
            _times[path] = mtime

        # Force restart when modification time has changed, even
        # if time now older, as that could indicate older file
        # has been restored.

        if mtime != _times[path]:
            return True
    except:
        # If any exception occured, likely that file has been
        # been removed just before stat(), so force a restart.

        return True

    return False

def _monitor():
    while 1:
        # Check modification times on all files in sys.modules.
        for folder in ['libs', 'apps']:
            for root, dirs, files in os.walk(os.path.join(os.path.dirname(__file__), folder)):
                for file in files:
                    path = os.path.join(root, file)
                    if os.path.splitext(path)[1] in ['.pyc', '.pyo', '.pyd']:
                        path = path[:-1]
                    if _modified(path):
                        return _restart(path)

        # Check modification times on files which have
        # specifically been registered for monitoring.

        for path in _files:
            if _modified(path):
                return _restart(path)

        # Go to sleep for specified interval.

        try:
            return _queue.get(timeout=_interval)
        except:
            pass

_thread = threading.Thread(target=_monitor)
_thread.setDaemon(True)

def _exiting():
    try:
        _queue.put(True)
    except:
        pass
    _thread.join()

atexit.register(_exiting)

def track(path):
    if not path in _files:
        _files.append(path)

def start(interval=1.0):
    global _interval
    if interval < _interval:
        _interval = interval

    global _running
    _lock.acquire()
    if not _running:
        prefix = 'monitor (pid=%d):' % os.getpid()
        print >> sys.stderr, '%s Starting change monitor.' % prefix
        _running = True
        _thread.start()
    _lock.release()

start(interval=1.0)

#

try:
    from local_settings import *
except:
    pass   
# ===============================================================================
