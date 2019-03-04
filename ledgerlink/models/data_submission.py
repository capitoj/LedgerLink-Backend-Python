from django.db import models

class DataSubmission(models.Model):

    id = models.AutoField(primary_key=True)
    SourceVslaCode = models.CharField(max_length=20, blank=True, null=True)
    SourcePhoneImei = models.CharField(max_length=20, blank=True, null=True)
    SourceNetworkOperator = models.CharField(max_length=50, blank=True, null=True)
    SourceNetworkType = models.CharField(max_length=20, blank=True, null=True)
    SubmissionTimestamp = models.DateTimeField(blank=True, null=True)
    Data = models.TextField(blank=True, null=True)
    ProcessedFlag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        default_permissions = ('add', 'change', 'delete', 'view', 'list')
        db_table = 'DataSubmission'

    def __str__(self):

        return self.SubmissionId

