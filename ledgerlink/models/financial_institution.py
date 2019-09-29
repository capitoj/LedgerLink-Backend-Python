from django.db import models

class FinancialInstitution(models.Model):

    id = models.AutoField(primary_key=True)
    FinancialInstitutionIdEx = models.IntegerField(blank=True, null=True)
    Name = models.CharField(max_length=255, blank=False, null=False)
    Code = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        managed = True
        default_permissions = ('add', 'change', 'delete', 'view', 'list')
        permissions = [
            ("post_bank_uganda", "can access Post Bank Uganda data"),
            ("finca_uganda_limited", "can access Finca Uganda Limited data"),
            ("barclays_bank_of_uganda", "can access Barclays Bank of Uganda data"),
            ("rural_finance_initiative", "can access Rural Finance Initiative data")
        ]
        db_table = 'FinancialInstitution'

    def __str__(self):

        return self.Name