# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 20:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20160407_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]