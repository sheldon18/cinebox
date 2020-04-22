# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-22 01:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20200421_2357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='release_date',
            new_name='release',
        ),
        migrations.AddField(
            model_name='movie',
            name='trailer',
            field=models.URLField(default='', max_length=254),
        ),
    ]