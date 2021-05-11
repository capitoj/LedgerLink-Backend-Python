from ledgerlink.models.vsla_credit_score import VslaCreditScore
from xf.xf_crud.model_forms import XFModelForm
import requests

class VslaCreditScoreForm(XFModelForm):

    def __init__(self, *args, **kwargs):
        super(VslaCreditScoreForm, self).__init__(*args, **kwargs)

        self.fields["RequestedLoanAmount"].label = "Loan Amount Requested"
        self.fields["DaysInArrears"].label = "Days in Arrears"
        self.fields["DaysInArrears"].widget.attrs['readonly'] = True

        self.fields["AmountInArrears"].label = "Amount In Arrears"
        self.fields["AmountInArrears"].widget.attrs['readonly'] = True

        self.fields["LoanRepaymentHistory"].label = "Loan Repayment History"
        self.fields["LoanRepaymentHistory"].widget.attrs['readonly'] = True

        self.fields["LoanRepaymentRate"].label = "Loan Repayment Rate"
        self.fields["LoanRepaymentRate"].widget.attrs['readonly'] = True

        self.fields["NumberOfLoansDisbursed"].label = "Number Of Loans Disbursed"
        self.fields["NumberOfLoansDisbursed"].widget.attrs['readonly'] = True

        self.fields["NumberOfYearsOfOperation"].label = "Number Of Years Of Operation"
        self.fields["NumberOfYearsOfOperation"].widget.attrs['readonly'] = True

        self.fields["AverageAttendanceRate"].label = "Average Attendance Rate"
        self.fields["AverageAttendanceRate"].widget.attrs['readonly'] = True

        self.fields["VolumeOfSavingsInPreviousCycle"].label = "Volume Of Savings In Previous Cycle"
        self.fields["VolumeOfSavingsInPreviousCycle"].widget.attrs['readonly'] = True

        self.fields["LoanFundUtilization"].label = "Loan Fund Utilization"
        self.fields["LoanFundUtilization"].widget.attrs['readonly'] = True

        self.fields["AverageSavingRateInCurrentCycle"].label = "Average Saving Rate In Current Cycle"
        self.fields["AverageSavingRateInCurrentCycle"].widget.attrs['readonly'] = True

        self.fields["PercentageOfMembersWithActiveLoan"].label = "Percentage of Members With Active Loans"
        self.fields["PercentageOfMembersWithActiveLoan"].widget.attrs['readonly'] = True

        self.fields["LoanWriteOffInPreviousCycle"].label = "Loan Write off In Previous Cycle"
        self.fields["LoanWriteOffInPreviousCycle"].widget.attrs['readonly'] = True

        self.fields["PortfolioAtRisk"].label = "Portfolio At Risk"
        self.fields["PortfolioAtRisk"].widget.attrs['readonly'] = True

        self.fields["FinalScore"].label = "Final Score"
        self.fields["FinalScore"].widget.attrs['readonly'] = True

        self.fields["Decision"].label = "Decision"
        self.fields["Decision"].widget.attrs['readonly'] = True

        self.fields["AssessmentAmount"].label = "Assessment Amount"
        self.fields["AssessmentAmount"].widget.attrs['readonly'] = True

        self.fields["DateProcessed"].label = "Date Processed"
        self.fields["DateProcessed"].widget.attrs['readonly'] = True

        self.fields["Vsla"].label = "Vsla Name"

    class Meta:
        model = VslaCreditScore
        title = "Vsla Credit Score"
        fields = ["id", "RequestedLoanAmount", "Vsla", "DaysInArrears", "AmountInArrears", "LoanRepaymentHistory", "LoanRepaymentRate", "NumberOfLoansDisbursed", "NumberOfYearsOfOperation", "AverageAttendanceRate", "VolumeOfSavingsInCurrentCycle", "VolumeOfSavingsInPreviousCycle", "LoanFundUtilization", "AverageSavingRateInCurrentCycle", "PercentageOfMembersWithActiveLoan", "LoanWriteOffInPreviousCycle", "PortfolioAtRisk", "FinalScore", "Decision", "AssessmentAmount", "DateProcessed"]

    def prepare_form_for_save(self, instance):

        instance = self.instance
        response = requests.get("http://127.0.0.1:82/loanperformer/getloanperformervariables/?vsla_id=" + self.request.POST["Vsla"] + "&requested_loan_amount=" + self.request.POST["RequestedLoanAmount"])
        if response.status_code == 200:
            json_data = response.json()
            if json_data["Status"] == "SUCCESSFUL":
                instance.DaysInArrears = json_data["DaysInArrears"]
                instance.AmountInArrears = json_data["AmountInArrears"]
                instance.LoanRepaymentHistory = json_data["LoanRepaymentHistory"]
                instance.LoanRepaymentRate = json_data["LoanRepaymentRate"]
                instance.NumberOfLoansDisbursed = json_data["NumberOfLoansDisbursed"]
                instance.NumberOfYearsOfOperation = json_data["NumberOfYearsOfOperation"]
                instance.AverageAttendanceRate = json_data["AverageAttendanceRate"]
                instance.VolumeOfSavingsInPreviousCycle = json_data["VolumeOfSavingsInPreviousCycle"]
                instance.LoanFundUtilization = json_data["LoanFundUtilization"]
                instance.AverageSavingRateInCurrentCycle = json_data["AverageSavingRateInCurrentCycle"]
                instance.PercentageOfMembersWithActiveLoan = json_data["PercentageOfMembersWithActiveLoan"]
                instance.LoanWriteOffInPreviousCycle = json_data["LoanWriteOffInPreviousCycle"]
                instance.PortfolioAtRisk = json_data["PortfolioAtRisk"]
                instance.FinalScore = json_data["FinalScore"]
                instance.Decision = json_data["Decision"]
                instance.AssessmentAmount = json_data["AssessmentAmount"]
                instance.DateProcessed = json_data["DateProcessed"]
                instance.PreviousLoanNumber = json_data["PreviousLoanNumber"]
                instance.VolumeOfSavingsInCurrentCycle = json_data["VolumeOfSavingsInCurrentCycle"]

                instance.save()
            else:
                instance.save(commit=False)
        else:
            instance.save(commit=False)

