# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-28 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20180628_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='output',
            name='Value1',
            field=models.FloatField(default=0.0),
        ),
    ]
