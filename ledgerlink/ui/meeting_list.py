from ledgerlink.models import Meeting
from xf.xf_crud.model_lists import XFModelList
from xf.xf_crud.xf_classes import XFUIAction, ACTION_ROW_INSTANCE


class MeetingList(XFModelList):

    def __init__(self, model):
        super(MeetingList, self).__init__(model)
        self.list_field_list = (
            "MeetingDate",
            "MeetingIdEx",
            "CountOfMembersPresent",
            "SumOfSavings",
            "SumOfLoanIssues",
            "SumOfLoanRepayments",
            "CashFines",
            "VslaCycle"
        )
        self.list_title = "VSLA Meeting List"
        self.search_hint = "Code, Name"
        self.list_hint = "Below are the list of VSLA meetings"
        self.supported_crud_operations.append("search")
        self.preset_filters = {'': 'All'}
        self.add_javascript("ledgerlink_vsla.js")


    def initialise_action_lists(self):
        self.instance_action_list.extend(
            (XFUIAction('overview', 'View details', 'view', action_type=ACTION_ROW_INSTANCE, use_ajax=False, column_index=1),)
        )

    def get_queryset(self, search_string, model, preset_filter, view_kwargs=None):
        if view_kwargs is not None:
            if "related_fk" in view_kwargs:
                return Meeting.objects.filter(VslaCycle_id = view_kwargs['related_fk'])
        return Meeting.objects.all()