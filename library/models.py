from __future__ import unicode_literals

from django.core.exceptions import ValidationError
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
        default_permissions = ('add', 'change', 'delete', 'view')



class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        default_permissions = ('add', 'change', 'delete', 'view')




class Book(models.Model):
    title = models.CharField(max_length=128)
    publication_date = models.DateField(blank=True, null=True)
    category = models.ForeignKey('Category', blank=True, null=True)
    author = models.ForeignKey('Author', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    class Meta:
        form_field_list = (("title", "publication_date", "category", "author"))
        list_description = "List of books below."
        list_title = "Our books"
        list_hint = "Below is a list of the books that you can borrow."
        default_permissions = ('add', 'change', 'delete', 'view')
        search_field = "title"
