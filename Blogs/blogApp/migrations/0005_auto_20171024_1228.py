# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-24 12:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0004_auto_20171023_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
