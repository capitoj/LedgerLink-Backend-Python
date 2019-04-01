from django.db import models

class Fine(models.Model):

    id = models.AutoField(primary_key=True)
    FineIdEx = models.IntegerField(blank=False, null=False)
    Amount = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    ExpectedDate = models.DateField(blank=True, null=True)
    IsCleared = models.IntegerField(blank=True, null=True)
    DateCleared = models.DateField(blank=True, null=True)
    IssuedInMeeting = models.ForeignKey("Meeting", related_name="fine_issued_in_meeting_id", blank=True, null=True, on_delete=models.PROTECT)
    PaidInMeeting = models.ForeignKey("Meeting", blank=True, related_name="fine_paid_in_meeting_id", null=True, on_delete=models.PROTECT)
    Member = models.ForeignKey("Member", blank=False, null=False, on_delete=models.PROTECT)
    IssuedInMeetingIdEx = models.IntegerField(blank=True, null=True)
    PaidInMeetingIdEx = models.IntegerField(blank=True, null=True)
    FineTypeId = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        default_permissions = ('add', 'change', 'delete', 'view', 'list')
        db_table = 'Fine'

    def __str__(self):
        return str(self.id)