# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-24 13:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0008_auto_20170924_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eorder',
            name='rec',
        ),
    ]
