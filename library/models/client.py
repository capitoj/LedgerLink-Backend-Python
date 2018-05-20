from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=256, null=False, blank=False)
    last_name = models.CharField(max_length=256, null=False, blank=False)
    registering_library = models.ForeignKey('Library', blank=False, null=False, related_name='registered_clients',
                                            on_delete=models.PROTECT)
    registration_date = models.DateField(blank=False, null=False)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

