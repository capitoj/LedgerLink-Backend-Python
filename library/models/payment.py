from django.db import models


class Payment(models.Model):
    checkout = models.ForeignKey('Checkout', blank=False, null=False, related_name='checkout_payments',
                                 on_delete=models.PROTECT)
    amount = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    payment_date = models.DateField(blank=False, null=False)
