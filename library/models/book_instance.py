from django.core.validators import RegexValidator
from django.db import models


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
