# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-06 20:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='production_company',
        ),
        migrations.AddField(
            model_name='movie',
            name='production_company',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='movies.Organization'),
            preserve_default=False,
        ),
    ]