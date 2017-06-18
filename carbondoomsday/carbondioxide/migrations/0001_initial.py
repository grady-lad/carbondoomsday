# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 07:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CO2Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('ppm', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
