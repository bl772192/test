# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-03 19:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='ticker',
            new_name='Parameter',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='close',
            new_name='Value',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='open',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='volume',
        ),
    ]