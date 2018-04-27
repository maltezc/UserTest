# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-11 14:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0025_auto_20180403_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='rating_dislikes',
            field=models.PositiveIntegerField(blank=True, default=0, editable=False),
        ),
        migrations.AddField(
            model_name='question',
            name='rating_likes',
            field=models.PositiveIntegerField(blank=True, default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to=settings.AUTH_USER_MODEL),
        ),
    ]