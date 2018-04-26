# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-19 03:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0013_gender_fixtures'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='gender',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='library.GenderCode'),
            preserve_default=False,
        ),
    ]