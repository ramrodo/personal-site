# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 18:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20170624_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 24, 13, 28, 32, 864240)),
        ),
    ]