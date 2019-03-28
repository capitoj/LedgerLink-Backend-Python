from django.db import models

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
    Meeting = models.ForeignKey("Meeting", blank=False, null=False, on_delete=models.PROTECT)
    Member = models.ForeignKey("Member", blank=False, null=False, on_delete=models.PROTECT)
    LoanId = models.ForeignKey("LoanIssue", blank=False, null=False, on_delete=models.PROTECT)

    class Meta:
        managed = True
        default_permissions = ('add', 'change', 'delete', 'view', 'list')
        db_table = 'LoanRepayment'

    def __str__(self):

        return self.id