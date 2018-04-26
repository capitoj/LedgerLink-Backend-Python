from __future__ import unicode_literals

import datetime

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models

from django.contrib.auth.models import User, Group

import django.db.models.options as options
options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('list_field_list', 'search_field', 'form_field_list', 'title',
    'list_description', 'list_title', 'list_hint')


from xf.xf_crud.models import XFCodeTable


class GenderCode(XFCodeTable):
    pass


class AuthorCategoryCode(XFCodeTable):
    pass



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



class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        default_permissions = ('add', 'change', 'delete', 'view', 'list')




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
    library = models.ForeignKey('Library', blank=False, null=True, related_name='book_instances',
                                on_delete=models.PROTECT)

    def __str__(self):
        return "%s (%s)" % (self.serial_number, self.book.title)


class Client(models.Model):
    first_name = models.CharField(max_length=256, null=False, blank=False)
    last_name = models.CharField(max_length=256, null=False, blank=False)
    registering_library = models.ForeignKey('Library', blank=False, null=False, related_name='registered_clients',
                                            on_delete=models.PROTECT)
    registration_date = models.DateField(blank=False, null=False)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Checkout(models.Model):

    def _get_default_checkin_date():
        checkout_date = datetime.date.today()
        allowed_period = datetime.timedelta(days=21)
        return checkout_date + allowed_period

    checkout_date = models.DateField(blank=False, null=False, default=datetime.date.today)
    required_checkin_date = models.DateField(blank=False, null=False, default=_get_default_checkin_date)
    client = models.ForeignKey('Client', blank=False, null=False, related_name='client_checkouts',
                               on_delete=models.PROTECT)
    price = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)

    def __str__(self):
        return "%s – %s" % (self.checkout_date, self.client)


class Payment(models.Model):
    checkout = models.ForeignKey('Checkout', blank=False, null=False, related_name='checkout_payments',
                                 on_delete=models.PROTECT)
    amount = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    payment_date = models.DateField(blank=False, null=False)


class CheckoutLine(models.Model):
    checkout = models.ForeignKey('Checkout', blank=False, null=False, related_name='checkout')
    book_instance = models.ForeignKey('BookInstance', blank=False, null=False, related_name='checkout_lines')
    checkout_date = models.DateField(blank=False, null=False)
    required_checkin_date = models.DateField(blank=False, null=False)
    actual_checkin_date = models.DateField(blank=True, null=True)

