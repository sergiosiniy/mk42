# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/migrations/0002_auto_20170614_1553.py

# Generated by Django 1.11.2 on 2017-06-14 15:53

from __future__ import unicode_literals

from django.db import migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="description",
            field=redactor.fields.RedactorField(blank=True, db_index=True, null=True, verbose_name="description"),
        ),
    ]