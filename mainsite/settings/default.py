from .base import *

DEBUG=True

HOME_PAGE = "/dashboards/page-section/default-perspective/home/"
LOGIN_URL = "/dashboards/page-section/login/"
LOGIN_REDIRECT_URL = "/"


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../default.sqlite3'),
    },
}
