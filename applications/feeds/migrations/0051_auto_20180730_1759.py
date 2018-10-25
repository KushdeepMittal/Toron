# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-30 12:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0050_auto_20180726_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Select_Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_tag_1', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='feeds.AllTags')),
            ],
        ),
        migrations.RemoveField(
            model_name='askaquestion',
            name='select_tag',
        ),
        migrations.AddField(
            model_name='askaquestion',
            name='select_tag',
            field=models.ManyToManyField(to='feeds.Select_Tag'),
        ),
    ]