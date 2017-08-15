from .base import *

DEBUG=False

#ALLOWED_HOSTS = ['localhost','127.0.0.1','ptbi-dashboard.globalhealthapp.net']
ALLOWED_HOSTS = ['*']
#USE_X_FORWARDED_HOST = True

DATABASES = {
    'default': {
        'NAME': 'moz_pmtct',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'postgres',
        'PORT': '5432',
        'HOST': 'localhost',
        'PASSWORD': '123ucsf456cqi789',
    },
    'supervision': {
        'NAME': 'odk_prod',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'reader',
        'PORT': '3306',
        'HOST': 'localhost',
        'PASSWORD': '???????????',
    }
}

STATIC_ROOT = '/var/www/ptv-dev.globalhealthapp.net/static/'

STATIC_URL = '/static/'


