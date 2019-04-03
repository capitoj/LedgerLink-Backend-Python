from ledgerlink.models import LoanRepayment
from xf.xf_crud.model_lists import XFModelList
from xf.xf_crud.xf_classes import XFUIAction, ACTION_ROW_INSTANCE

class LoanRepaymentList(XFModelList):

    def __init__(self, model):
        super(LoanRepaymentList, self).__init__(model)

        self.list_field_list = (
            "LoanIssue",
            "Member",
            "Amount",
            "BalanceBefore",
            "BalanceAfter",
            "LastDueDate",
            "NextDueDate",
            "InterestAmount",
            "Meeting"
        )
        self.list_title = "Loan Repayments"
        self.search_hint = "Search by StartDate, EndDate, InterestRate"
        self.supported_crud_operations.append('search')
        self.list_hint = "Below is a list of loan repayments"

    def initialise_action_lists(self):
        self.row_action_list.extend(
            (XFUIAction('overview', 'View details', 'view', action_type=ACTION_ROW_INSTANCE, use_ajax=False,
                        column_index=1),)
        )

    def get_queryset(self, search_string, model, preset_filter, view_kwargs=None):
        if view_kwargs is not None:
            if "related_fk" in view_kwargs:
                return LoanRepayment.objects.filter(Meeting_id = view_kwargs['related_fk'])
        return LoanRepayment.objects.all()