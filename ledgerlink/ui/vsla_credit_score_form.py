from django.forms import forms

from ledgerlink.models.vsla_credit_score import VslaCreditScore
from xf.xf_crud.model_forms import XFModelForm

class VslaCreditScoreForm(XFModelForm):

    def __init__(self, *args, **kwargs):
        super(VslaCreditScoreForm, self).__init__(*args, **kwargs)
        self.fields["NumberOfYearsOfOperation"].label = "# Years of Operation"
        # self.fields["NumberOfYearsOfOperation"].widget.
        self.fields["LoanRepaymentHistory"].label = "Repayment History"
        self.fields["AverageAttendanceRate"].label = "Attendance Rate"
        self.fields["AverageSavingRate"].label = "Savings Rate"
        self.fields["SecondLastCycleShareOutAmount"].label = "2nd Last Cycle Share-out Amount"
        self.fields["LoanLossRate"].label = "Loan Loss Rate"
        self.fields["FinalScore"].label = "Final Score"
        self.fields["Decision"].label = "Decision"
        self.fields["ODAmount"].label = "Amount"

    class Meta:
        model = VslaCreditScore
        title = "Vsla Credit Score"
        fields = ["id",
                  "NumberOfYearsOfOperation",
                  "LoanRepaymentHistory",
                  "AverageAttendanceRate",
                  "AverageSavingRate",
                  "SecondLastCycleShareOutAmount",
                  "LastCycleShareOutAmount",
                  "LoanLossRate",
                  "FinalScore",
                  "Decision",
                  "ODAmount"]