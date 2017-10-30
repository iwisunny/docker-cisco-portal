# coding: utf-8
# Django settings for webappcenter project.
import os

# if DEBUG is True, DB Queries are cached,
# and 404 / exception page will use Django debug page
# set DEBUG = False, so 404 page will use your customed one
DEBUG = False

# if TEMPLATE_DEBUG is True, error page will provide extra infomation
TEMPLATE_DEBUG = DEBUG

BASE = '/pitrix/lib/pitrix-webappcenter'

# don't set ADMINS, use log
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': '',   # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',     # Or path to database file if using sqlite3.
        'USER': '',     # Not used with sqlite3.
        'PASSWORD': '', # Not used with sqlite3.
        'HOST': '',     # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',     # Set to empty string for default. Not used with sqlite3.
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
    ('zh-cn', gettext('Chinese Simplified')),
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
# Example: '/home/media/media.lawrence.com/media/'
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: 'http://media.lawrence.com/media/', 'http://example.com/media/'
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' 'static/' subdirectories and in STATICFILES_DIRS.
# Example: '/home/media/media.lawrence.com/static/'
STATIC_ROOT = ''

# URL prefix for static files.
# Example: 'http://media.lawrence.com/static/'
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like '/home/html/static' or 'C:/www/django/static'.
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/pitrix/lib/pitrix-webappcenter/static',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '$05qc+eei&p+zknktkw@ehu_e+#%d%sc1wy2s+ev8iii*j*s4y'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'mysite.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like '/home/html/django_templates'
    # or 'C:/www/django/templates'.
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/pitrix/lib/pitrix-webappcenter/templates',
)

INSTALLED_APPS = (
    'mysite.apps.custom',
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
        # memcache server
        # DON'T MODIFY THIS LINE
        'LOCATION': 'memcache:11211',
    }
}

# SESSION
SESSION_COOKIE_NAME = 'sid'
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7

# Using Memcache as session storage backend
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# Using File as session storage backend
#SESSION_ENGINE = 'django.contrib.sessions.backends.file'
#SESSION_FILE_PATH = '/tmp'

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
    'download_root': '/pitrix/lib/pitrix-webappcenter/storage',

    # static file root
    'static_file_root': '/pitrix/lib/pitrix-webappcenter/static',

    # restrict admin requests in this server port,
    # if port is '', all admin requests is allowed
    'admin_server_port': '8081',

    # auto version will turned on if True and close if False
    'auto_version': True,

    # enable signup function
    'enable_signup': True,

    # public zones that can be access by newly registered user
    'public_zones': ['pek2', 'gd1'],

    # api server
    'api_server': {
        'host': 'api.staging.com', # staging
        'port': 80,
        'protocol': 'http',
        'session_uri': '/i2/',
        'console_uri': '/i3/',
        'msg_time_out': 10,
        'http_socket_timeout': 15,
        'console_key_id': '',
        'console_secrect_key': '',
    },
}

SITE_URL = 'https://www.qingcloud.com'
CONSOLE_URL = 'https://console.qingcloud.com'
PUSH_URL = 'https://console.qingcloud.com:8000'
DOCS_URL = 'https://docs.qingcloud.com'

try:
    from local_settings import *
except:
    pass
