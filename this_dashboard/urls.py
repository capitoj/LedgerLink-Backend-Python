from django.conf.urls import url

from this_dashboard.widget_views import widget_blank, widget_current_time, widget_preterm_tiles, WCurrentTime, \
    WDiagnosisList, WDiagnosisPie, WModesOfDeliveryPie
from views import UDSDashboardPageView
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^dashboards/uds/(?P<section>[-\w]+)/(?P<slug>[-\w]+)/$', UDSDashboardPageView.as_view(), name='uds'),
    url(r'^dashboards/widgets/blank', widget_blank, name='widget_blank'),
    url(r'^dashboards/widgets/current_time', WCurrentTime.as_view(), name='widget_current_time'),
    url(r'^dashboards/widgets/diagnosis_list', WDiagnosisList.as_view(), name='widget_diagnosis_list'),
    url(r'^dashboards/widgets/diagnosis_pie', WDiagnosisPie.as_view(), name='widget_diagnosis_pie'),
    url(r'^dashboards/widgets/modes_of_delivery_pie', WModesOfDeliveryPie.as_view(), name='widget_modes_of_delivery_pie'),
    url(r'^dashboards/widgets/preterm_tiles', widget_preterm_tiles, name='widget_preterm_tiles'),
    ]
