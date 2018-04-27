from .base import *
from .default import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db_unittest.sqlite3',
    },
}

