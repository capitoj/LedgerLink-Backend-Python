from django.db import models

class Member(models.Model):

    id = models.AutoField(primary_key=True)
    MemberIdEx = models.IntegerField(blank=True, null=True)
    MemberNo = models.IntegerField(blank=True, null=True)
    CyclesCompleted = models.IntegerField(blank=True, null=True)
    Surname = models.CharField(max_length=30, blank=False, null=False)
    OtherNames = models.CharField(max_length=50, blank=True, null=True)
    Gender = models.CharField(max_length=10, blank=True, null=True)
    Occupation = models.CharField(max_length=50, blank=True, null=True)
    DateArchived = models.DateField(blank=True, null=True)
    DateOfBirth = models.DateField(blank=True, null=True)
    IsActive = models.IntegerField(blank=True, null=True)
    IsArchived = models.IntegerField(blank=True, null=True)
    PhoneNo = models.CharField(max_length=20, blank=True, null=True)
    VslaId = models.ForeignKey("Vsla", blank=False, null=False, on_delete=models.PROTECT)

    class Meta:
        managed = True
        default_permissions = ('add', 'change', 'delete', 'view', 'list')
        db_table = 'Member'

    def __str__(self):

        return "%s %s" % (self.Surname, self.OtherNames)