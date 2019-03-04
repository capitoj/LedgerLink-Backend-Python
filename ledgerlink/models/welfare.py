from django.db import models

class Welfare(models.Model):

    id = models.AutoField(primary_key=True)
    WelfareIdEx = models.IntegerField(blank=True, null=True)
    Amount = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    Comment = models.CharField(max_length=150, blank=True, null=True)
    MeetingId = models.ForeignKey("Meeting", blank=False, null=False, on_delete=models.PROTECT)
    MemberId = models.ForeignKey("Member", blank=False, null=False, on_delete=models.PROTECT)

    class Meta:
        managed = True
        default_permissions = ('add', 'change', 'delete', 'view', 'list')
        db_table = 'Welfare'

    def __str__(self):

        return self.WelfareId