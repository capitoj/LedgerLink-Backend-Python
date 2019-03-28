from django.db import models

class Saving(models.Model):

    id = models.AutoField(primary_key=True)
    SavingIdEx = models.IntegerField(blank=True, null=True)
    Amount = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    Meeting = models.ForeignKey("Meeting", blank=False, null=False, on_delete=models.PROTECT)
    Member = models.ForeignKey("Member", blank=False, null=False, on_delete=models.PROTECT)

    class Meta:
        managed = True
        default_permissions = ('add', 'change', 'delete', 'view', 'list')
        db_table = 'Saving'

    def __str__(self):

        return self.SavingId