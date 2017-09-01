import pymysql
import sys

pymysql.install_as_MySQLdb()

if len(sys.argv) > 1:
    if sys.argv[1] != "makemigrations" and sys.argv[1] != "migrate":
        default_app_config = 'mainsite.apps.XFMainAppConfig'