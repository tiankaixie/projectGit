# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-13 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='featurePicture',
            field=models.CharField(default='#', max_length=150),
        ),
        migrations.AddField(
            model_name='historyperiod',
            name='featurePicture',
            field=models.CharField(default='#', max_length=150),
        ),
    ]
