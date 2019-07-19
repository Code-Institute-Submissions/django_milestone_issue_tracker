# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-19 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0002_commentfeature_upvotefeature'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='quantity',
            field=models.DecimalField(decimal_places=0, default='1', max_digits=1),
        ),
        migrations.AddField(
            model_name='feature',
            name='vote_price',
            field=models.DecimalField(decimal_places=2, default=5, max_digits=6),
        ),
    ]