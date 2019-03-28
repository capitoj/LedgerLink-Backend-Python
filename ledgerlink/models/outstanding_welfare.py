from django.db import models

class OutstandingWelfare(models.Model):

    id = models.AutoField(primary_key=True)
    OutstandingWelfareIdEx = models.IntegerField(blank=True, null=True)
    Amount = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    ExpectedDate = models.DateField(blank=True, null=True)
    IsCleared = models.IntegerField(blank=True, null=True)
    DateCleared = models.DateField(blank=True, null=True)
    PaidInMeeting = models.ForeignKey("Meeting", related_name="outstanding_welfare_paid_in_meeting_id", blank=False, null=False, on_delete=models.PROTECT)
    Comment = models.CharField(max_length=150, blank=True, null=True)
    Meeting = models.ForeignKey("Meeting", related_name="outstanding_welfare_issued_in_meeting_id", blank=False, null=False, on_delete=models.PROTECT)
    Member = models.ForeignKey("Member", blank=False, null=False, on_delete=models.PROTECT)

    class Meta:
        managed = True
        default_permissions = ('add', 'change', 'delete', 'view', 'list')
        db_table = 'OutstandingWelfare'

    def __str__(self):

        return self.OutstandingWelfareId