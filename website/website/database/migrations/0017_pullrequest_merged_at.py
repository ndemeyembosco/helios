# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2021-05-21 22:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0016_auto_20210519_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='pullrequest',
            name='merged_at',
            field=models.DateTimeField(null=True),
        ),
    ]