# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 18:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20170628_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 28, 18, 23, 21, 971770, tzinfo=utc)),
        ),
    ]