# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-15 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_auto_20180315_0411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='user',
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='question',
            name='answer_html',
            field=models.TextField(default=''),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
