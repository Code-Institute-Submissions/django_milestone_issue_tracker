# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-18 17:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('upvotes', models.IntegerField(default='0')),
                ('views', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('T', 'To Do'), ('P', 'In Progress'), ('C', 'Complete')], default='T', max_length=1)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]