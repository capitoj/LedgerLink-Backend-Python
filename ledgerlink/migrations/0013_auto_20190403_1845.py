# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-04-03 15:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ledgerlink', '0012_auto_20190331_2346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loanrepayment',
            old_name='LoanId',
            new_name='LoanIssue',
        ),
    ]
