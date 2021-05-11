from ledgerlink.models.vsla_credit_score import VslaCreditScore
from xf.xf_crud.model_lists import XFModelList

class VslaCreditScoreList(XFModelList):

    def __init__(self, model):
        super(VslaCreditScoreList, self).__init__(model)
        self.list_field_list = (
            "RequestedLoanAmount",
                  "NumberOfYearsOfOperation",
                  "AverageAttendanceRate",
                  "LoanFundUtilization",
                  "PortfolioAtRisk",
                  "FinalScore",
                  "AssessmentAmount",
                  "DateProcessed"
        )
        self.list_title = "Credit Scores"
        self.list_hint = "List of previous credit scores"

    def get_queryset(self, search_string, model, preset_filter, view_kwargs=None):
        if view_kwargs is not None:
            if "related_fk" in view_kwargs:
                return VslaCreditScore.objects.filter(Vsla_id = view_kwargs["related_fk"])
        return VslaCreditScore.objects.all()