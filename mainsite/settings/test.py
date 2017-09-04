from .base import *

DEBUG=True

#ALLOWED_HOSTS = ['localhost','127.0.0.1','ptbi-dashboard.globalhealthapp.net']
ALLOWED_HOSTS = ['*']
#USE_X_FORWARDED_HOST = True

DATABASES = {
    'default': {
        'NAME': 'ptbi_dashboard_test',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'dashboard',
        'PORT': '3306',
        'HOST': 'localhost',
        'PASSWORD': 'dashboard',
    },
    'ptbi_data': {
        'NAME': 'ptbi_bi',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'readonly',
        'PORT': '3306',
        'HOST': 'localhost',
        'PASSWORD': 'readonly',
    }
}

STATIC_ROOT = '/var/www/xf_sample_test.globalhealthapp.net/static/'

STATIC_URL = '/static/'


