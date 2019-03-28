from django.db import models

class Meeting(models.Model):

    id = models.AutoField(primary_key=True)
    MeetingIdEx = models.IntegerField(blank=False, null=False)
    CashExpenses = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    CashFines = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    CashFromBox = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    CashSavedBank = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    CashSavedBox = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    CashWelfare = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    DateSent = models.DateField(blank=True, null=True)
    IsCurrent = models.IntegerField(blank=True, null=True)
    IsDataSent = models.IntegerField(blank=True, null=True)
    MeetingDate = models.DateField(blank=True, null=True)
    CountOfMembersPresent = models.IntegerField(blank=True, null=True)
    SumOfSavings = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    SumOfLoanIssues = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    SumOfLoanRepayments = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    Cycle = models.ForeignKey("VslaCycle", blank=False, null=False, on_delete=models.PROTECT)
    LoanFromBank = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    BankLoanRepayment = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)

    class Meta:
        managed = True
        default_permissions = ('add', 'change', 'delete', 'view', 'list')
        db_table = 'Meeting'

    def __str__(self):

        return "%s-%s" % (self.id, self.MeetingDate)