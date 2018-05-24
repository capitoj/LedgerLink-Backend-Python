from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)
    gender = models.ForeignKey('GenderCode', blank=False, null=False, on_delete=models.PROTECT)
    category = models.ForeignKey('AuthorCategoryCode', blank=False, null=False, on_delete=models.PROTECT)

    def __str__(self):

        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        default_permissions = ('add', 'change', 'delete', 'view', 'list')

    def prepare_for_save(self, request, user):

        pass
