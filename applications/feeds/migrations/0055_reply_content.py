# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-02 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0054_auto_20180802_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='content',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
