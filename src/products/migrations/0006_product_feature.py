# -*- coding: utf-8 -*-
# Generated by Django 1.11.15.dev20190124060509 on 2019-01-24 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20190123_0653'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='feature',
            field=models.BooleanField(default=False),
        ),
    ]
