# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 18:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20161102_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='r_projektbild',
            name='projekt_f',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.R_Projekt'),
            preserve_default=False,
        ),
    ]
