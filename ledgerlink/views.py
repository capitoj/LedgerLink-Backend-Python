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

        vsla_members_instance = XFDivLoader()
        vsla_members_instance.caption = "Members"
        vsla_members_instance.url = reverse('crud_savings-group-members_list_by-vsla', kwargs={'related_fk': self.kwargs['pk']}) + "?&embed"
        self.add_related_listview(vsla_members_instance)

        vsla_creditscore_instancce = XFDivLoader()
        vsla_creditscore_instancce.caption = "Credit Score"
        vsla_creditscore_instancce.url = reverse('crud_savings-group-credit-score_list_by-vsla',
                                                       kwargs={'related_fk': self.kwargs['pk']}) + "?&embed"
        self.add_related_listview(vsla_creditscore_instancce)

        return context

class VslaCycleMasterChildView(XFMasterChildView):
    template_name = "form_master_child.html"

    def get_context_data(self, **kwargs):
        context = super(VslaCycleMasterChildView, self).get_context_data(**kwargs)

        vsla_cycle_meeting_instance = XFDivLoader()
        vsla_cycle_meeting_instance.caption = "Vsla Meetings"
        vsla_cycle_meeting_instance.url = reverse('crud_savings-group-cycle-meeting_list_by-cycle',  kwargs={'related_fk':self.kwargs['pk']})+ "?&embed"
        self.add_related_listview(vsla_cycle_meeting_instance)

        vsla_cycle_creditscore_instancce = XFDivLoader()
        vsla_cycle_creditscore_instancce.caption = "Credit Score"
        vsla_cycle_creditscore_instancce.url = reverse('crud_savings-group-cycle-meeting_list_by-cycle',  kwargs={'related_fk':self.kwargs['pk']})+ "?&embed"
        self.add_related_listview(vsla_cycle_creditscore_instancce)

        return context


class VslaCycleMeetingMasterChildView(XFMasterChildView):
    template_name = "form_master_child.html"

    def get_context_data(self, **kwargs):
        context = super(VslaCycleMeetingMasterChildView, self).get_context_data(**kwargs)

        vsla_cycle_meeting_attendance = XFDivLoader();
        vsla_cycle_meeting_attendance.caption = "Attendance"
        vsla_cycle_meeting_attendance.url = reverse('crud_savings-group-cycle-meeting-attendance_list_by-meeting-attendance', kwargs={'related_fk':self.kwargs['pk']})+ "?&embed"
        self.add_related_listview(vsla_cycle_meeting_attendance)

        vsla_cycle_meeting_saving = XFDivLoader();
        vsla_cycle_meeting_saving.caption = "Savings"
        vsla_cycle_meeting_saving.url = reverse('crud_savings-group-cycle-meeting-saving_list_by-meeting-saving', kwargs={'related_fk':self.kwargs['pk']})+ "?&embed"
        self.add_related_listview(vsla_cycle_meeting_saving)

        vsla_cycle_meeting_fines = XFDivLoader();
        vsla_cycle_meeting_fines.caption = "Fines"
        vsla_cycle_meeting_fines.url = reverse('crud_savings-group-cycle-meeting-fine_list_by-meeting-fine',
                                                kwargs={'related_fk': self.kwargs['pk']}) + "?&embed"
        self.add_related_listview(vsla_cycle_meeting_fines)

        vsla_cycle_meeting_loan_issue = XFDivLoader();
        vsla_cycle_meeting_loan_issue.caption = "Loan Issues"
        vsla_cycle_meeting_loan_issue.url = reverse('crud_savings-group-cycle-meeting-loan-issue_list_by-meeting-loan-issue',
                                               kwargs={'related_fk': self.kwargs['pk']}) + "?&embed"
        self.add_related_listview(vsla_cycle_meeting_loan_issue)

        vsla_cycle_meeting_loan_repayment = XFDivLoader();
        vsla_cycle_meeting_loan_repayment.caption = "Loan Repayment"
        vsla_cycle_meeting_loan_repayment.url = reverse(
            'crud_savings-group-cycle-meeting-loan-repayment_list_by-meeting-loan-repayment',
            kwargs={'related_fk': self.kwargs['pk']}) + "?&embed"
        self.add_related_listview(vsla_cycle_meeting_loan_repayment)

        vsla_cycle_meeting_welfare = XFDivLoader();
        vsla_cycle_meeting_welfare.caption = "Welfare"
        vsla_cycle_meeting_welfare.url = reverse(
            'crud_savings-group-cycle-meeting-welfare_list_by-meeting-welfare',
            kwargs={'related_fk': self.kwargs['pk']}) + "?&embed"
        self.add_related_listview(vsla_cycle_meeting_welfare)

        vsla_cycle_meeting_outstanding_welfare = XFDivLoader();
        vsla_cycle_meeting_outstanding_welfare.caption = "Outstanding Welfare"
        vsla_cycle_meeting_outstanding_welfare.url = reverse(
            'crud_savings-group-cycle-meeting-outstanding-welfare_list_by-meeting-outstanding-welfare',
            kwargs={'related_fk': self.kwargs['pk']}) + "?&embed"
        self.add_related_listview(vsla_cycle_meeting_outstanding_welfare)

        return context