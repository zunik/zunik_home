# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 23:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0006_auto_20170923_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video_type',
        ),
    ]
