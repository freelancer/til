# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 04:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tilweb', '0002_auto_20170831_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
