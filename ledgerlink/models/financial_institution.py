from django.db import models

class FinancialInstitution(models.Model):

    id = models.AutoField(primary_key=True)
    FinancialInstitutionIdEx = models.IntegerField(blank=True, null=True)
    Name = models.CharField(max_length=255, blank=False, null=False)
    Code = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        managed = True
        default_permissions = ('add', 'change', 'delete', 'view', 'list')
        db_table = 'FinancialInstitution'

    def __str__(self):

        return self.Name