from django.db import models

from ledgerlink.models import VslaRegion
from ledgerlink.models.financial_institution import FinancialInstitution
from ledgerlink.models.technical_trainer import TechnicalTrainer


class Vsla(models.Model):

    id = models.AutoField(primary_key=True)
    VslaCode = models.CharField(max_length=255, blank=False, null=False)
    VslaName = models.CharField(max_length=255, blank=False, null=False)
    VslaPhoneMsisdn = models.CharField(max_length=20, blank=True, null=True)
    PhysicalAddress = models.CharField(max_length=255, blank=True, null=True)
    GpsLocation = models.CharField(max_length=100, blank=True, null=True)
    DateRegistered = models.DateField(blank=True, null=True)
    DateLinked = models.DateField(blank=True, null=True)
    Region = models.ForeignKey(VslaRegion, blank=False, null=False, on_delete=models.PROTECT)
    ContactPerson = models.CharField(max_length=250, blank=True, null=True)
    PositionInVsla = models.CharField(max_length=100, blank=True, null=True)
    PhoneNumber = models.CharField(max_length=50, blank=True, null=True)
    TechnicalTrainer = models.ForeignKey(TechnicalTrainer, blank=False, null=False, on_delete=models.PROTECT)
    Status = models.IntegerField(blank=False, null=False)
    GroupAccountNumber = models.CharField(max_length=250, blank=True, null=True)
    NumberOfCycles = models.IntegerField(blank=True, null=True)
    Implementer = models.CharField(max_length=200, blank=True, null=True)
    FinancialInstitution = models.ForeignKey(FinancialInstitution, blank=False, null=False, on_delete=models.PROTECT)

    class Meta:
        managed = True
        default_permissions = ('add', 'change', 'delete', 'view', 'list')
        db_table = 'Vsla'

    def __str__(self):
        return self.VslaName
