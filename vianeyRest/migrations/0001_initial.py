# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-24 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreMateria', models.CharField(blank=True, default='', max_length=100)),
                ('primerParcialMateria', models.CharField(blank=True, default='', max_length=100)),
                ('segundoParcialMateria', models.CharField(blank=True, default='', max_length=100)),
                ('tercerParcialMateria', models.CharField(blank=True, default='', max_length=100)),
                ('ordinarioMateria', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'ordering': ('nombreMateria',),
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePersona', models.CharField(blank=True, default='', max_length=100)),
                ('apeliidoPPersona', models.CharField(blank=True, default='', max_length=100)),
                ('apellidoMPersona', models.CharField(blank=True, default='', max_length=100)),
                ('licenciaturaPersona', models.CharField(blank=True, default='', max_length=100)),
                ('semestrePersona', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'ordering': ('nombrePersona',),
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreUsuario', models.CharField(blank=True, default='', max_length=100)),
                ('contrasenaUsuario', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'ordering': ('nombreUsuario',),
            },
        ),
    ]
