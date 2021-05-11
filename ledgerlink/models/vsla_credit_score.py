from django.db import models

from ledgerlink.models.vsla import Vsla

class VslaCreditScore(models.Model):

    id = models.AutoField(primary_key=True)
    RequestedLoanAmount = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=False)
    DaysInArrears = models.IntegerField(blank=True, null=False)
    AmountInArrears = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=False)
    LoanRepaymentHistory = models.CharField(max_length=200, blank=True, null=False)
    LoanRepaymentRate = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=False)
    NumberOfLoansDisbursed = models.IntegerField(blank=True, null=False)
    NumberOfYearsOfOperation = models.IntegerField(blank=True, null=False)
    AverageAttendanceRate = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    VolumeOfSavingsInPreviousCycle = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=False)
    LoanFundUtilization = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=False)
    AverageSavingRateInCurrentCycle = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=False)
    PercentageOfMembersWithActiveLoan = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    LoanWriteOffInPreviousCycle = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    PortfolioAtRisk = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=False)
    FinalScore = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=False)
    Decision = models.CharField(max_length=255, blank=True, null=False)
    AssessmentAmount = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    Vsla = models.ForeignKey(Vsla, blank=False, null=False, on_delete=models.PROTECT)
    DateProcessed = models.DateField(blank=True, null=True)
    PreviousLoanNumber = models.CharField(max_length=200, blank=True, null=True)
    VolumeOfSavingsInCurrentCycle = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    FilePath = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        default_permissions = ('add', 'change', 'delete', 'view', 'list')
        db_table = "VslaCreditScore"

    def __str__(self):
        return "%s" % (self.AssessmentAmount)