# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2021-05-11 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledgerlink', '0020_vslacreditscore_previousloannumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='vslacreditscore',
            name='VolumeOfSavingsInCurrentCycle',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
