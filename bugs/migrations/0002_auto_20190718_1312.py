# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-18 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='name',
            field=models.CharField(default='', max_length=254),
        ),
    ]