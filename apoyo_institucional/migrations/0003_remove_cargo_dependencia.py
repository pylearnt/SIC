# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-09 23:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apoyo_institucional', '0002_auto_20161209_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cargo',
            name='dependencia',
        ),
    ]
