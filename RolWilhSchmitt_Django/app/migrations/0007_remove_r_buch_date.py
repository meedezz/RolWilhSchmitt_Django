# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 22:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_r_buch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='r_buch',
            name='date',
        ),
    ]
