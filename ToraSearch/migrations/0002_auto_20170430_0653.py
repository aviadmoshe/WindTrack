# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-30 03:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToraSearch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadtoratext',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='yeshiva',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
