# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-11 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20170111_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]