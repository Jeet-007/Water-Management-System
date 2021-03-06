# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-11 08:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0005_actuator'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensordata',
            name='read_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
