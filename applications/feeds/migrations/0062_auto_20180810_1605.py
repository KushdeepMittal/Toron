# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-10 10:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0061_auto_20180810_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='askaquestion',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
