# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-25 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0044_remove_comments_likes_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
