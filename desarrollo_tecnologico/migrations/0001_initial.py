# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 22:12
from __future__ import unicode_literals

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nucleo', '0001_initial'),
        ('publicacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClasificacionProyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clasificacion', models.CharField(max_length=255, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='clasificacion', unique=True)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Clasificación de proyectos',
                'verbose_name': 'Clasificación de proyecto',
            },
        ),
        migrations.CreateModel(
            name='DesarrolloTecnologico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_desarrollo_tecnologico', models.CharField(max_length=255, unique=True)),
                ('descripcion', models.TextField()),
                ('version', models.CharField(max_length=100)),
                ('patente', models.CharField(blank=True, max_length=255)),
                ('url', models.URLField(blank=True)),
                ('fecha', models.DateField()),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=models.CharField(max_length=255, unique=True), unique=True)),
                ('agradecimientos', models.ManyToManyField(related_name='desarrollo_tecnologico_agradecimientos', to=settings.AUTH_USER_MODEL)),
                ('autores', models.ManyToManyField(related_name='desarrollo_tecnologico_autores', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Desarrollos Tecnológicos',
                'ordering': ['nombre_desarrollo_tecnologico'],
                'get_latest_by': ['fecha', 'nombre_desarrollo_tecnologico'],
            },
        ),
        migrations.CreateModel(
            name='FinanciamientoExterno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('clave_proyecto', models.CharField(max_length=255)),
                ('dependencias_financiamiento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='financiamiento_externo_dependencias_financiamiento', to='nucleo.Programa')),
            ],
            options={
                'verbose_name_plural': 'Financiamientos (externos)',
                'ordering': ['financiamiento'],
                'verbose_name': 'Financiamiento (externo)',
            },
        ),
        migrations.CreateModel(
            name='FinanciamientoUNAM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('clave_proyecto', models.CharField(max_length=255)),
                ('dependencias_financiamiento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='financiamiento_unam_dependencias_financiamiento', to='nucleo.Programa')),
            ],
            options={
                'verbose_name_plural': 'Financiamientos UNAM',
                'ordering': ['financiamiento'],
                'verbose_name': 'Financiamiento UNAM',
            },
        ),
        migrations.CreateModel(
            name='Licencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('licencia', models.CharField(max_length=255, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='licencia', unique=True)),
                ('descripcion', models.TextField()),
                ('url', models.URLField()),
            ],
            options={
                'ordering': ['licencia'],
            },
        ),
        migrations.CreateModel(
            name='Metodologia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metodologia', models.CharField(max_length=255, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='metodologia', unique=True)),
                ('descripcion', models.TextField()),
            ],
            options={
                'ordering': ['metodologia'],
            },
        ),
        migrations.CreateModel(
            name='ModalidadProyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modalidad', models.CharField(max_length=255, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='modalidad', unique=True)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Organizaciones de proyectos',
                'verbose_name': 'Organización de proyecto',
            },
        ),
        migrations.CreateModel(
            name='OrganizacionProyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organizacion', models.CharField(max_length=255, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='organizacion', unique=True)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Organizaciones de proyectos',
                'verbose_name': 'Organización de proyecto',
            },
        ),
        migrations.CreateModel(
            name='ProblemaNacional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problema', models.CharField(max_length=255, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='problema', unique=True)),
                ('descripcion', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Tipos de problemas nacionales',
                'ordering': ['problema'],
                'verbose_name': 'Tipo de problema nacional',
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True)),
                ('es_permanente', models.BooleanField(default=False)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField(blank=True)),
                ('tematica_genero', models.BooleanField(default=False)),
                ('alumnos_doctorado', models.ManyToManyField(related_name='proyecto_investigacion_alumnos_doctorado', to=settings.AUTH_USER_MODEL)),
                ('alumnos_licenciatura', models.ManyToManyField(related_name='proyecto_investigacion_alumnos_licenciatura', to=settings.AUTH_USER_MODEL)),
                ('alumnos_maestria', models.ManyToManyField(related_name='proyecto_investigacion_alumnos_maestria', to=settings.AUTH_USER_MODEL)),
                ('areas_wos', models.ManyToManyField(related_name='proyecto_investigacion_areas_wos', to='publicacion.AreaWOS')),
                ('clasificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='desarrollo_tecnologico.ClasificacionProyecto')),
                ('dependencias_internacionales', models.ManyToManyField(related_name='proyecto_investigacion_dependencias_internacionales', to='nucleo.Dependencia')),
                ('dependencias_otras', models.ManyToManyField(related_name='proyecto_investigacion_dependencias_otras', to='nucleo.Dependencia')),
                ('dependencias_sic', models.ManyToManyField(related_name='proyecto_investigacion_dependencias_sic', to='nucleo.Dependencia')),
                ('dependencias_unam', models.ManyToManyField(related_name='proyecto_investigacion_dependencias_unam', to='nucleo.Dependencia')),
                ('especialidades', models.ManyToManyField(related_name='proyecto_investigacion_especialidades', to='publicacion.Especialidad')),
                ('financiamientos_externo', models.ManyToManyField(blank=True, to='desarrollo_tecnologico.FinanciamientoExterno')),
                ('financiamientos_unam', models.ManyToManyField(blank=True, to='desarrollo_tecnologico.FinanciamientoUNAM')),
                ('impactos_sociales', models.ManyToManyField(related_name='proyecto_investigacion_impactos_sociales', to='nucleo.ImpactoSocial')),
                ('metodologias', models.ManyToManyField(related_name='proyecto_investigacion_metodologias', to='desarrollo_tecnologico.Metodologia')),
                ('modalidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='desarrollo_tecnologico.ModalidadProyecto')),
                ('organizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='desarrollo_tecnologico.OrganizacionProyecto')),
                ('participantes', models.ManyToManyField(related_name='proyecto_investigacion_participantes', to=settings.AUTH_USER_MODEL)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.Region')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['fecha_inicio', 'nombre'],
            },
        ),
        migrations.CreateModel(
            name='StatusProyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=255, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='status', unique=True)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Status de proyectos',
                'verbose_name': 'Status de proyecto',
            },
        ),
        migrations.CreateModel(
            name='TipoDesarrollo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_desarrollo', models.CharField(max_length=255, unique=True)),
                ('descripcion', models.TextField()),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='tipo_desarrollo', unique=True)),
            ],
            options={
                'verbose_name_plural': 'Tipos de desarrollo',
                'ordering': ['tipo_desarrollo'],
                'verbose_name': 'Tipo de desarrollo',
            },
        ),
        migrations.CreateModel(
            name='TipoFinanciamientoExterno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_financiamiento', models.CharField(max_length=255, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='tipo_financiamiento', unique=True)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Tipos de Financiamiento (externo)',
                'ordering': ['tipo_financiamiento'],
                'verbose_name': 'Tipo de Financiamiento (externo)',
            },
        ),
        migrations.CreateModel(
            name='TipoParticipacionProyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=255, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='tipo', unique=True)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Tipos de participación en proyectos',
                'verbose_name': 'Tipo de participación en proyecto',
            },
        ),
        migrations.CreateModel(
            name='TipoPresupuestoUNAM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_presupuesto', models.CharField(max_length=255, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='tipo_presupuesto', unique=True)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Tipos de Presupuesto UNAM',
                'ordering': ['tipo_presupuesto'],
                'verbose_name': 'Tipo de Presupuesto UNAM',
            },
        ),
        migrations.CreateModel(
            name='TipoProblemaNacional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_problema', models.CharField(max_length=255, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='tipo_problema', unique=True)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Tipos de problemas nacionales',
                'verbose_name': 'Tipo de problema nacional',
            },
        ),
        migrations.AddField(
            model_name='proyecto',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='desarrollo_tecnologico.StatusProyecto'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='tecnicos',
            field=models.ManyToManyField(related_name='proyecto_investigacion_impactos_tecnicos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='tipo_participacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='desarrollo_tecnologico.TipoParticipacionProyecto'),
        ),
        migrations.AddField(
            model_name='problemanacional',
            name='tipo_problema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='desarrollo_tecnologico.TipoProblemaNacional'),
        ),
        migrations.AddField(
            model_name='financiamientounam',
            name='financiamiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='desarrollo_tecnologico.TipoPresupuestoUNAM'),
        ),
        migrations.AddField(
            model_name='financiamientounam',
            name='programas_financiamiento',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='financiamiento_unam_programas_financiamiento', to='nucleo.Programa'),
        ),
        migrations.AddField(
            model_name='financiamientoexterno',
            name='financiamiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='desarrollo_tecnologico.TipoFinanciamientoExterno'),
        ),
        migrations.AddField(
            model_name='financiamientoexterno',
            name='programas_financiamiento',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='financiamiento_externo_programas_financiamiento', to='nucleo.Programa'),
        ),
        migrations.AddField(
            model_name='desarrollotecnologico',
            name='licencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='desarrollo_tecnologico.Licencia'),
        ),
        migrations.AddField(
            model_name='desarrollotecnologico',
            name='proyectos',
            field=models.ManyToManyField(related_name='desarrollo_tecnologico_proyectos', to='desarrollo_tecnologico.Proyecto'),
        ),
        migrations.AddField(
            model_name='desarrollotecnologico',
            name='tags',
            field=models.ManyToManyField(related_name='desarrollo_tecnologico_tags', to='nucleo.Tag'),
        ),
        migrations.AddField(
            model_name='desarrollotecnologico',
            name='tipo_desarrollo_tecnologico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='desarrollo_tecnologico.TipoDesarrollo'),
        ),
    ]
