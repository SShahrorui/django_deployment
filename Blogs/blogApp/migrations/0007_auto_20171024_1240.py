# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-24 12:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0006_auto_20171024_1235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='approved_comment',
            new_name='approved_comments',
        ),
    ]
