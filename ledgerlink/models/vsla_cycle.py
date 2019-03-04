from django.db import models

class VslaCycle(models.Model):

    id = models.AutoField(primary_key=True)
    CycleIdEx = models.IntegerField(blank=True, null=True)
    DateEnded = models.DateField(blank=True, null=True)
    EndDate = models.DateField(blank=True, null=True)
    CycleCode = models.CharField(max_length=20, blank=True, null=True)
    InterestRate = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    IsEnded = models.IntegerField(blank=True, null=True)
    MaxShareQuantity = models.IntegerField(blank=True, null=True)
    MaxStartShare = models.IntegerField(blank=True, null=True)
    SharedAmount = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    SharePrice = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    ShareDate = models.DateField(blank=True, null=True)
    VslaId = models.ForeignKey("Vsla", blank=False, null=False, on_delete=models.PROTECT)
    MigratedInterest = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    MigratedFines = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)

    class Meta:
        managed = True
        default_permissions = ('add', 'change', 'delete', 'view', 'list')
        db_table = 'VslaCycle'

    def __str__(self):
        return self.CycleId

