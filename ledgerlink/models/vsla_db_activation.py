from django.db import models

class VslaDbActivation(models.Model):

    id = models.AutoField(primary_key=True)
    ActivationDate = models.DateField(blank=True, null=True)
    IsActive = models.IntegerField(blank=True, null=True)
    PassKey = models.CharField(max_length=255, blank=True, null=True)
    PhoneImei1 = models.CharField(max_length=255, blank=True, null=True)
    PhoneImei2 = models.CharField(max_length=255, blank=True, null=True)
    SimImsiNo01 = models.CharField(max_length=255, blank=True, null=True)
    SimImsiNo02 = models.CharField(max_length=255, blank=True, null=True)
    SimNetworkOperator01 = models.CharField(max_length=255, blank=True, null=True)
    SimNetworkOperator02 = models.CharField(max_length=255, blank=True, null=True)
    SimSerialNo01 = models.CharField(max_length=255, blank=True, null=True)
    SimSerialNo02 = models.CharField(max_length=255, blank=True, null=True)
    VslaId = models.ForeignKey("Vsla", blank=False, null=False, on_delete=models.PROTECT)

    class Meta:
        managed = True
        default_permissions = ('add', 'change', 'delete', 'view', 'list')
        db_table = 'VslaDbActivation'

    def __str__(self):

        return self.ActivationId
