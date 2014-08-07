import os.path
import dj_database_url

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))



DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
)

MANAGERS = ADMINS

DATABASES = {}
DATABASES['default'] =  dj_database_url.config(default=os.environ['DATABASE_URL'])


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

ALLOWED_HOSTS = []

TIME_ZONE = 'Asia/Tehran'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = ""

MEDIA_URL = '/media/'

STATIC_ROOT = ROOT + "/static"

STATIC_URL = '/static/'


STATICFILES_DIRS = (
	ROOT + "/staticfiles",
)


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


SECRET_KEY = 'x3xy=l0p+n!)mc0@&d_$b$3epvvc0kl7=rbu+++)_4z!2+6tbz'


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.gzip.GZipMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
)

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
SESSION_COOKIE_HTTPONLY = True


ROOT_URLCONF = 'AdvidiTest.urls'


WSGI_APPLICATION = 'AdvidiTest.wsgi.application'

TEMPLATE_DIRS = (
	ROOT + "/templates",
)

INSTALLED_APPS = (
	'django.contrib.staticfiles',
	'campaigns',
)



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
