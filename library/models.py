from __future__ import unicode_literals

import datetime

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models

from django.contrib.auth.models import User, Group

import django.db.models.options as options
options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('list_field_list', 'search_field', 'form_field_list', 'title',
    'list_description', 'list_title', 'list_hint')


class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        default_permissions = ('add', 'change', 'delete', 'view', 'list')



class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        default_permissions = ('add', 'change', 'delete', 'view', 'list')




class Book(models.Model):
    title = models.CharField(max_length=128)
    publication_date = models.DateField(blank=True, null=True)
    category = models.ForeignKey('Category', blank=True, null=True)
    author = models.ForeignKey('Author', blank=True, null=True, on_delete=models.SET_NULL)

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




class Library(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)

    def __str__(self):
        return self.name


class BookInstance(models.Model):
    serial_number = models.CharField(max_length=128,
                                     blank=False, null=False,
                                     unique=True,
                                     validators=[
                                         RegexValidator(
                                             regex=r'\d{3}-\d{4}?$',
                                             message="Please use xxx-xxxx",
                                         )
                                     ])
    book = models.ForeignKey('Book', blank=False, null=True, related_name='instances')
    library = models.ForeignKey('Library', blank=False, null=True, related_name='book_instances')

    def __str__(self):
        return "%s (%s)" % (self.serial_number, self.book.title)

