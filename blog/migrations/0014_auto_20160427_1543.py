# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20160427_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='hobby',
            field=models.TextField(blank=True, null=True, unique=True),
        ),
    ]