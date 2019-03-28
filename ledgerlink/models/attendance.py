from django.db import models

class Attendance(models.Model):

    id = models.AutoField(primary_key=True)
    AttendanceIdEx = models.IntegerField(blank=True, null=True)
    Comments = models.CharField(max_length=150, blank=True, null=True)
    IsPresent = models.IntegerField(blank=True, null=True)
    Meeting = models.ForeignKey("Meeting", blank=False, null=False, on_delete=models.PROTECT)
    Member = models.ForeignKey("Member", blank=False, null=False, on_delete=models.PROTECT)

    class Meta:
        managed = True
        default_permissions = ('add', 'change', 'delete', 'view', 'list')
        db_table = 'Attendance'

    def __str__(self):

        return "%s" % self.id