from django.db import models

class VslaBankingHistory(models.Model):

    id = models.AutoField(primary_key=True)
    AccountNumber = models.CharField(max_length=255, blank=True, null=True)
    AccountName = models.CharField(max_length=255, blank=True, null=True)
    Amount = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    Status = models.CharField(max_length=50, blank=True, null=True)
    Month = models.CharField(max_length=50, blank=True, null=True)
    Year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        default_permissions = ('add', 'change', 'delete', 'view', 'list')
        db_table = 'VslaBankingHistory'

    def __str__(self):

        return self.BankingHistoryId