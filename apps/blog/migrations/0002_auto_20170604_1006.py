# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-04 15:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 4, 10, 6, 33, 483308)),
        ),
    ]
