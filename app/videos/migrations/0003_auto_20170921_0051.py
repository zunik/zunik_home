# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 00:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_auto_20170921_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_at',
            field=models.DateField(),
        ),
    ]