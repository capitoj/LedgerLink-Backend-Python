
from django.apps import AppConfig
from django.db import connection



class XFMainAppConfig(AppConfig):

    name = 'mainsite'
    verbose_name = "My XF Application"

    def ready(self):

        from xf.xf_system.models import XFSiteSettings
        from xf.xf_system.views import XFNavigationViewMixin

        table_exists = False

        try:
            table_exists = "xf_system_xfsitesettings" in connection.introspection.table_names()
            settings = XFSiteSettings.objects.filter(settings_key='default')
        except:
            settings = None
            pass

        if table_exists is False or settings.count() == 0:
            print("No settings")
            XFNavigationViewMixin.site_settings = XFSiteSettings()
            XFNavigationViewMixin.site_settings.site_title = "XF"
            XFNavigationViewMixin.site_settings.settings_key = "undefined"
            XFNavigationViewMixin.site_settings.site_icon = "fa-globe"
            XFNavigationViewMixin.site_settings.footer_details = "'institution_name':'XF',"
        else:
            XFNavigationViewMixin.site_settings = settings[0]

        pass # startup code here
