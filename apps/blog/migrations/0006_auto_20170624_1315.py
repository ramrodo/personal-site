# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 18:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170624_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 24, 13, 15, 46, 407250)),
        ),
    ]
