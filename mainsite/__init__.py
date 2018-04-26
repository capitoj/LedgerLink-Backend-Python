#import pymysql
import sys

#pymysql.install_as_MySQLdb()



if len(sys.argv) > 1:
    if sys.argv[1] != "makemigrations" and sys.argv[1] != "migrate" and sys.argv[1] != "test2":
        default_app_config = 'mainsite.apps.XFMainAppConfig'


# https://docs.djangoproject.com/en/1.11/ref/applications/#django.apps.AppConfig.ready
# https://stackoverflow.com/questions/6791911/execute-code-when-django-starts-once-only