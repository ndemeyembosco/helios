# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2021-02-22 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_auto_20210221_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commit',
            name='branch',
            field=models.CharField(default='master', max_length=512),
        ),
    ]