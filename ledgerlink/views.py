from xf.xf_crud.generic_crud_views import XFMasterChildView
from xf.xf_crud.model_lists import XFDivLoader
from django.urls import reverse

class VslaMasterChildView(XFMasterChildView):
    template_name = "form_master_child.html"

    def get_context_data(self, **kwargs):
        context = super(VslaMasterChildView, self).get_context_data(**kwargs)

        vsla_instance = XFDivLoader();
        vsla_instance.caption = "Vsla Cycles"
        vsla_instance.url = reverse('crud_savings-group-cycle_list_by-vsla',  kwargs={'related_fk':self.kwargs['pk']})+ "?&embed"
        self.add_related_listview(vsla_instance)

        # widget = XFDivLoader()
        # widget.caption = "Statistics"
        # widget.url = "http://127.0.0.1:8001/widgets/mean-bruto/"
        # self.add_related_listview(widget)

        return context

class VslaInstanceMasterChildView(XFMasterChildView):
    template_name = "form_master_child.html"

    def get_context_data(self, **kwargs):
        context = super(VslaInstanceMasterChildView, self).get_context_data(**kwargs)

        vsla_cycle_instance = XFDivLoader();
        vsla_cycle_instance.caption = "Vsla Meetings"
        vsla_cycle_instance.url = reverse('crud_savings-group-meeting_list_by-cycle',  kwargs={'related_fk':self.kwargs['pk']})+ "?&embed"
        self.add_related_listview(vsla_cycle_instance)

        return context


class VslaCycleInstanceMasterChildView(XFMasterChildView):
    template_name = "form_master_child.html"

    def get_context_data(self, **kwargs):
        context = super(VslaCycleInstanceMasterChildView, self).get_context_data(**kwargs)

        vsla_cycle_instance = XFDivLoader();
        vsla_cycle_instance.caption = "Vsla Meetings"
        vsla_cycle_instance.url = reverse('crud_savings-group-meeting_list_by-cyclex',  kwargs={'related_fk':self.kwargs['pk']})+ "?&embed"
        self.add_related_listview(vsla_cycle_instance)

        return context


class MeetingAttendanceMasterChildView(XFMasterChildView):
    template_name = "form_master_child.html"

    def get_context_data(self, **kwargs):
        context = super(MeetingAttendanceMasterChildView, self).get_context_data(**kwargs)

        vsla_cycle_instance = XFDivLoader();
        vsla_cycle_instance.caption = "Vsla Meetings"
        vsla_cycle_instance.url = reverse('crud_savings-group-meeting-attendance_list_by-meeting',  kwargs={'related_fk':self.kwargs['pk']})+ "?&embed"
        self.add_related_listview(vsla_cycle_instance)

        return context