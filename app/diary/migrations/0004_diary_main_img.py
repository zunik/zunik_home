# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-04 00:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_diary_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='main_img',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]