import datetime

from django.core.exceptions import ValidationError
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=128)
    publication_date = models.DateField(blank=True, null=True)
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.PROTECT)
    author = models.ForeignKey('Author', blank=True, null=True, on_delete=models.PROTECT)

    @property
    def instance_count(self):
        return self.instances.count()



    def __str__(self):
        return self.title

    class Meta:
        default_permissions = ('add', 'change', 'delete', 'view', 'list')


    def clean(self):

        validation_errors = {}

        if self.title.find("23") >= 0:
            validation_errors['title'] = ValidationError("Can't have the word 23 in the title.")

        if self.publication_date:
            if self.publication_date > datetime.datetime.today().date():
                validation_errors['publication_date'] = ValidationError("Cannot be in the future.")

            if self.publication_date < datetime.date(1900, 1, 1):
                validation_errors['publication_date'] = ValidationError("Try a date from 1900 onwards.")

        if validation_errors:
            raise ValidationError(validation_errors)

