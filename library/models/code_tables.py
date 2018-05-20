from django.db import models

from xf.xf_crud.models import XFCodeTable


class GenderCode(XFCodeTable):
    pass


class AuthorCategoryCode(XFCodeTable):
    pass

class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        default_permissions = ('add', 'change', 'delete', 'view', 'list')

