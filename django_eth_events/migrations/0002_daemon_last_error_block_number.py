# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-16 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_eth_events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='daemon',
            name='last_error_block_number',
            field=models.IntegerField(default=0),
        ),
    ]
