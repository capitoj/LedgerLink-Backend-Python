from django.db import models

from ledgerlink.models.meeting import Meeting
from ledgerlink.models.member import Member

class LoanIssue(models.Model):

    id = models.AutoField(primary_key=True)
    LoanIdEx = models.IntegerField(blank=True, null=True)
    LoanNo = models.IntegerField(blank=True, null=True)
    PrincipalAmount = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    InterestAmout = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    Balance = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    Comments = models.CharField(max_length=150, blank=True, null=True)
    DateCleared = models.DateField(blank=True, null=True)
    DueDate = models.DateField(blank=True, null=True)
    IsCleared = models.IntegerField(blank=True, null=True)
    IsDefaulted = models.IntegerField(blank=True, null=True)
    TotalRepaid = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    IsWrittenOff = models.IntegerField(blank=True, null=True)
    Meeting = models.ForeignKey(Meeting, blank=False, null=False, on_delete=models.PROTECT)
    Member = models.ForeignKey(Member, blank=False, null=False, on_delete=models.PROTECT)

    class Meta:
        managed = True
        default_permissions = ('add', 'change', 'delete', 'view', 'list')
        db_table = 'LoanIssue'

    def __str__(self):
        return str(self.id)