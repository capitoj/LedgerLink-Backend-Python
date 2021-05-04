from django.db import models

from ledgerlink.models.vsla import Vsla

class VslaCreditScore(models.Model):

    id = models.AutoField(primary_key=True)
    NumberOfYearsOfOperation = models.IntegerField(blank=True, null=False)
    LoanRepaymentHistory = models.CharField(max_length=200, blank=True, null=False)
    AverageAttendanceRate = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=False)
    AverageSavingRate = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=False)
    SecondLastCycleShareOutAmount = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    LastCycleShareOutAmount = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    LoanLossRate = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=False)
    FinalScore = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=False)
    Decision = models.CharField(max_length=255, blank=True, null=False)
    ODAmount = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    Vsla = models.ForeignKey(Vsla, blank=False, null=False, on_delete=models.PROTECT)

    class Meta:
        managed = True
        default_permissions = ('add', 'change', 'delete', 'view', 'list')
        db_table = "VslaCreditScore"

    def __str__(self):
        return "%s" % (self.ODAmount)