# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-12 21:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0004_diary_main_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='recommend',
            field=models.BooleanField(default=False),
        ),
    ]
