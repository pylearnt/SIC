# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 23:08
from __future__ import unicode_literals

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nucleo', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actividad', models.CharField(max_length=255, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='actividad', unique=True)),
            ],
            options={
                'verbose_name_plural': 'Actividades',
            },
        ),
        migrations.CreateModel(
            name='ApoyoOtraActividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('apoyo_inicio', models.DateField()),
                ('apoyo_fin', models.DateField()),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='apoyo_actividad', unique=True)),
                ('apoyo_actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apoyo_institucional.Actividad')),
                ('dependencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.Dependencia')),
                ('tags', models.ManyToManyField(to='nucleo.Tag')),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.Ubicacion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Apoyos en Otras Actividades',
                'ordering': ['-apoyo_inicio'],
                'get_latest_by': ['user', 'apoyo_actividad'],
            },
        ),
        migrations.CreateModel(
            name='ApoyoTecnico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('apoyo_inicio', models.DateField()),
                ('apoyo_fin', models.DateField()),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='apoyo_tecnico', unique=True)),
                ('apoyo_tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apoyo_institucional.Actividad')),
                ('dependencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.Dependencia')),
                ('tags', models.ManyToManyField(to='nucleo.Tag')),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.Ubicacion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Apoyos de Técnicos',
                'ordering': ['-apoyo_inicio'],
                'get_latest_by': ['user', 'apoyo_tecnico'],
            },
        ),
        migrations.CreateModel(
            name='CargoAcademicoAdministrativo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo_inicio', models.DateField()),
                ('cargo_fin', models.DateField()),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='cargo', unique=True)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.Cargo')),
                ('dependencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.Dependencia')),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.Ubicacion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Cargos Académico-Administrativos',
                'ordering': ['-cargo_inicio'],
                'get_latest_by': ['user', 'cargo'],
            },
        ),
        migrations.CreateModel(
            name='Comision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comision', models.CharField(max_length=255, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='comision', unique=True)),
            ],
            options={
                'verbose_name_plural': 'Comisiones',
            },
        ),
        migrations.CreateModel(
            name='ComisionAcademica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('comision_inicio', models.DateField()),
                ('comision_fin', models.DateField()),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='comision_academica', unique=True)),
                ('comision_academica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apoyo_institucional.Comision')),
                ('dependencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.Dependencia')),
                ('tags', models.ManyToManyField(to='nucleo.Tag')),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.Ubicacion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Comisiones Académicas',
                'ordering': ['-comision_inicio'],
                'get_latest_by': ['user', 'comision_academica'],
            },
        ),
        migrations.CreateModel(
            name='ComisionEvaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('es_academica', models.BooleanField(default=False)),
                ('comision_inicio', models.DateField()),
                ('comision_fin', models.DateField()),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='comision_evaluacion', unique=True)),
                ('comision_evaluacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apoyo_institucional.Comision')),
                ('dependencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.Dependencia')),
                ('tags', models.ManyToManyField(to='nucleo.Tag')),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.Ubicacion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Comisiones de Evaluación',
                'ordering': ['-comision_inicio'],
                'get_latest_by': ['user', 'comision_evaluacion'],
            },
        ),
        migrations.CreateModel(
            name='OrganoColegiado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organo_colegiado', models.CharField(max_length=255, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='organo_colegiado', unique=True)),
            ],
            options={
                'verbose_name_plural': 'Organos Colegiados',
            },
        ),
        migrations.CreateModel(
            name='Representante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('representante', models.CharField(max_length=255, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='representante', unique=True)),
            ],
            options={
                'verbose_name_plural': 'Representantes',
            },
        ),
        migrations.CreateModel(
            name='RepresentanteAnteOrganoColegiado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo_inicio', models.DateField()),
                ('cargo_fin', models.DateField()),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='representante', unique=True)),
                ('dependencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.Dependencia')),
                ('organo_colegiado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apoyo_institucional.OrganoColegiado')),
                ('representante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apoyo_institucional.models.Representacion')),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.Ubicacion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Representantes Ante Organos Colegiados',
                'ordering': ['-cargo_inicio'],
                'get_latest_by': ['user', 'organo_colegiado', 'representante'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='representanteanteorganocolegiado',
            unique_together=set([('representante', 'organo_colegiado', 'user', 'dependencia', 'cargo_inicio')]),
        ),
        migrations.AlterUniqueTogether(
            name='comisionevaluacion',
            unique_together=set([('comision_evaluacion', 'user', 'dependencia', 'comision_inicio')]),
        ),
        migrations.AlterUniqueTogether(
            name='comisionacademica',
            unique_together=set([('comision_academica', 'user', 'dependencia', 'comision_inicio')]),
        ),
        migrations.AlterUniqueTogether(
            name='cargoacademicoadministrativo',
            unique_together=set([('cargo', 'user', 'dependencia', 'cargo_inicio')]),
        ),
        migrations.AlterUniqueTogether(
            name='apoyotecnico',
            unique_together=set([('apoyo_tecnico', 'user', 'dependencia', 'apoyo_inicio')]),
        ),
        migrations.AlterUniqueTogether(
            name='apoyootraactividad',
            unique_together=set([('apoyo_actividad', 'user', 'dependencia', 'apoyo_inicio')]),
        ),
    ]