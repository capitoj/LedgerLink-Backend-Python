from xf.xf_crud.model_lists import XFModelList
from xf.xf_crud.xf_classes import XFUIAction

class MeetingList(XFModelList):

    def __init__(self, model):
        super(MeetingList, self).__init__(model)
        self.list_field_list = ("MeetingIdEx", "MeetingDate", "CountOfMembersPresent", "SumOfSavings", "SumOfLoanIssues", "SumOfLoanRepayments", "CashFines")
        self.list_title = "VSLA Meeting List"
        self.search_hint = "Code, Name"
        self.list_hint = "Below are the list of VSLA meetings"
        self.supported_crud_operations.append("search")
        self.preset_filters = {'': 'All'}
        self.add_javascript("ledgerlink_vsla.js")

        self.row_action_list.append(XFUIAction('overview', 'View Meetings', 'view', use_ajax=False, column_index=1))