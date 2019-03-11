from django.contrib import admin

from ledgerlink.models import TechnicalTrainer, FinancialInstitution, Vsla, VslaCycle, Meeting, Attendance, Saving, \
    Fine, LoanRepayment, LoanIssue, Member, DataSubmission, VslaDbActivation, VslaBankingHistory
from .models import VslaRegion

admin.site.register(VslaRegion)
admin.site.register(TechnicalTrainer)
admin.site.register(FinancialInstitution)
admin.site.register(Vsla)
admin.site.register(VslaCycle)
admin.site.register(Meeting)
admin.site.register(Attendance)
admin.site.register(Saving)
admin.site.register(Fine)
admin.site.register(LoanRepayment)
admin.site.register(LoanIssue)
admin.site.register(Member)
admin.site.register(DataSubmission)
admin.site.register(VslaDbActivation)
admin.site.register(VslaBankingHistory)