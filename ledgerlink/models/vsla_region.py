from django.db import models


class VslaRegion(models.Model):
    id = models.AutoField(primary_key=True)
    RegionCode = models.CharField(max_length=255, blank=True, null=True)
    RegionName = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        default_permissions = ('add', 'change', 'delete', 'view', 'list')
        db_table = 'VslaRegion'

    def __str__(self):
        return "%s" % self.RegionName
