from django.shortcuts import render

# Create your views here.
from xf.uc_dashboards.views.dashboard_page_view import DashboardPageView


class UDSDashboardPageView(DashboardPageView):

    def get_context_data(self, **kwargs):
        context = super(UDSDashboardPageView, self).get_context_data(**kwargs)

        context["widget1"] = "Hello world"
        context["widget1_data_percent"] = "60"

        data = {}
        data["data_percent"] = "40"
        context["data1"] = data

        data = {}
        data["data_percent"] = "81"
        context["data2"] = data

        data = {}
        data["data_percent"] = "39"
        context["data3"] = data

        return context

