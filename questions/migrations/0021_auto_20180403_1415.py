# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-03 14:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0020_comment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
