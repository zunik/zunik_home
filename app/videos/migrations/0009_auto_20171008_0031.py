# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 00:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0008_video_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['-video_at']},
        ),
    ]
