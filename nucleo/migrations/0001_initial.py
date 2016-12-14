# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 10:29
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='ciudad')),
            ],
            options={
                'ordering': ['estado', 'ciudad'],
                'verbose_name_plural': 'Ciudades',
            },
        ),
        migrations.CreateModel(
            name='Dependencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dependencia', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='dependencia')),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='estado')),
            ],
            options={
                'ordering': ['pais', 'estado'],
            },
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institucion', models.CharField(max_length=255, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='institucion')),
            ],
            options={
                'verbose_name_plural': 'Instituciones',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=200, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='pais')),
                ('codigo', models.SlugField(max_length=2, unique=True)),
            ],
            options={
                'ordering': ['pais'],
                'verbose_name_plural': 'Paises',
                'verbose_name': 'País',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='tag')),
            ],
            options={
                'ordering': ['tag'],
            },
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion1', models.CharField(max_length=255, verbose_name='Dirección')),
                ('direccion2', models.CharField(blank=True, max_length=255, verbose_name='Dirección (continuación)')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='direccion1')),
                ('codigo_postal', models.IntegerField()),
                ('telefono', models.SlugField(max_length=20)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.Ciudad')),
            ],
            options={
                'verbose_name_plural': 'Ubicaciones',
            },
        ),
        migrations.AddField(
            model_name='institucion',
            name='ubicacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.Ubicacion'),
        ),
        migrations.AddField(
            model_name='estado',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.Pais'),
        ),
        migrations.AddField(
            model_name='dependencia',
            name='institucion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.Institucion'),
        ),
        migrations.AddField(
            model_name='dependencia',
            name='ubicacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.Ubicacion'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.Estado'),
        ),
        migrations.AlterUniqueTogether(
            name='ubicacion',
            unique_together=set([('direccion1', 'direccion2', 'ciudad')]),
        ),
        migrations.AlterUniqueTogether(
            name='estado',
            unique_together=set([('estado', 'pais')]),
        ),
        migrations.AlterUniqueTogether(
            name='dependencia',
            unique_together=set([('dependencia', 'institucion')]),
        ),
        migrations.AlterUniqueTogether(
            name='ciudad',
            unique_together=set([('ciudad', 'estado')]),
        ),
    ]
