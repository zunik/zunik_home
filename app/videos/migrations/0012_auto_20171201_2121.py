# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-01 21:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0011_favoritevideo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favoritevideo',
            options={'ordering': ['-id']},
        ),
    ]
