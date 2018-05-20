import datetime

from django.db import models


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




class CheckoutLine(models.Model):
    checkout = models.ForeignKey('Checkout', blank=False, null=False, related_name='checkout')
    book_instance = models.ForeignKey('BookInstance', blank=False, null=False, related_name='checkout_lines')
    checkout_date = models.DateField(blank=False, null=False)
    required_checkin_date = models.DateField(blank=False, null=False)
    actual_checkin_date = models.DateField(blank=True, null=True)

