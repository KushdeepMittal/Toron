# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-01 11:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0002_auto_20180401_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='askaquestion',
            name='uploaded_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
