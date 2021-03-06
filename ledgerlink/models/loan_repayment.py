from django.db import models
from ledgerlink.models.meeting import Meeting
from ledgerlink.models.member import Member
from ledgerlink.models.loan_issue import LoanIssue

class LoanRepayment(models.Model):

    id = models.AutoField(primary_key=True)
    RepaymentIdEx = models.IntegerField(blank=True, null=True)
    Amount = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    BalanceAfter = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    BalanceBefore = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    Comments = models.CharField(max_length=150, blank=True, null=True)
    LastDueDate = models.DateField(blank=True, null=True)
    NextDueDate = models.DateField(blank=True, null=True)
    InterestAmount = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    RolloverAmount = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    Meeting = models.ForeignKey(Meeting, blank=False, null=False, on_delete=models.PROTECT)
    Member = models.ForeignKey(Member, blank=False, null=False, on_delete=models.PROTECT)
    LoanIssue = models.ForeignKey(LoanIssue, blank=False, null=True, on_delete=models.PROTECT)

    class Meta:
        managed = True
        default_permissions = ('add', 'change', 'delete', 'view', 'list')
        db_table = 'LoanRepayment'

    def __str__(self):
        return str(self.id)