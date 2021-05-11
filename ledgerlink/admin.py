from django.contrib import admin

from ledgerlink.models.vsla_region import VslaRegion
from ledgerlink.models.vsla import Vsla
from ledgerlink.models.member import Member
from ledgerlink.models.vsla_cycle import VslaCycle
from ledgerlink.models.data_submission import DataSubmission
from ledgerlink.models.meeting import Meeting
from ledgerlink.models.attendance import Attendance
from ledgerlink.models.fine import Fine
from ledgerlink.models.loan_issue import LoanIssue
from ledgerlink.models.loan_repayment import LoanRepayment
from ledgerlink.models.outstanding_welfare import OutstandingWelfare
from ledgerlink.models.saving import Saving
from ledgerlink.models.technical_trainer import TechnicalTrainer
from ledgerlink.models.welfare import Welfare
from ledgerlink.models.financial_institution import FinancialInstitution
from ledgerlink.models.vsla_db_activation import VslaDbActivation
from ledgerlink.models.vsla_banking_history import VslaBankingHistory
from ledgerlink.models.vsla_credit_score import VslaCreditScore

admin.site.register(VslaRegion)
admin.site.register(TechnicalTrainer)
admin.site.register(FinancialInstitution)
admin.site.register(Vsla)
admin.site.register(VslaCycle)
admin.site.register(Meeting)
admin.site.register(Attendance)
admin.site.register(Welfare)
admin.site.register(Saving)
admin.site.register(Fine)
admin.site.register(LoanRepayment)
admin.site.register(LoanIssue)
admin.site.register(OutstandingWelfare)
admin.site.register(Member)
admin.site.register(DataSubmission)
admin.site.register(VslaDbActivation)
admin.site.register(VslaBankingHistory)
admin.site.register(VslaCreditScore)