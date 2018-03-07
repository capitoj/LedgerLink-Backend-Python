from .base import *

DEBUG=True

#ALLOWED_HOSTS = ['localhost','127.0.0.1','ptbi-dashboard.globalhealthapp.net']
ALLOWED_HOSTS = ['*']
#USE_X_FORWARDED_HOST = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../default.sqlite3'),
    },
}
