# -*- coding: utf-8 -*-
# Generated by Django 1.11.15.dev20190208030303 on 2019-02-10 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0006_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='last4',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]