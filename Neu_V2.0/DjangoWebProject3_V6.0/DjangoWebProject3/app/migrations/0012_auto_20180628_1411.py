# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-28 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20180628_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='output',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
