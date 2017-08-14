
from django.apps import AppConfig




class XFMainAppConfig(AppConfig):

    name = 'mainsite'
    verbose_name = "My XF Application"

    def ready(self):

        from xf_system.models import XFSiteSettings
        from xf_system.views import XFNavigationViewMixin

        settings = XFSiteSettings.objects.filter(settings_key='default')

        if not settings:
            print("No settings")
            XFNavigationViewMixin.site_settings = XFSiteSettings()
            XFNavigationViewMixin.site_settings.site_title = "XF"
            XFNavigationViewMixin.site_settings.settings_key = "undefined"
            XFNavigationViewMixin.site_settings.site_icon = "fa-globe"
        else:
            XFNavigationViewMixin.site_settings = settings[0]

        pass # startup code here

