from django.db import models

from ledgerlink.models import VslaRegion


class TechnicalTrainer(models.Model):

    id = models.AutoField(primary_key=True)
    Region = models.ForeignKey(VslaRegion, blank=False, null=False, on_delete=models.PROTECT)
    PhoneNumber = models.CharField(max_length=50, blank=False, null=False)
    Email = models.EmailField(blank=False, null=False)
    Status = models.IntegerField(blank=False, null=False)
    FirstName = models.CharField(max_length=150, blank=True, null=True)
    LastName = models.CharField(max_length=150, blank=True, null=True)
    Username = models.CharField(max_length=50, blank=False, null=False)
    PassKey = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        managed = True
        default_permissions = ('add', 'change', 'delete', 'view', 'list')
        db_table = 'TechnicalTrainer'

    def __str__(self):
        return "%s %s" % (self.FirstName, self.LastName)