# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-15 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20180315_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.TextField(default='', unique=True),
        ),
    ]
