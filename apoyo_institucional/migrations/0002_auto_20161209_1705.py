# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-09 23:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apoyo_institucional', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='dependencia',
            unique_together=set([('nombre', 'institucion')]),
        ),
    ]
