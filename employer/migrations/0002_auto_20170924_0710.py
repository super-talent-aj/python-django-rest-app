# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-23 23:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='employee_count',
            field=models.CharField(blank=True, choices=[('0<10', '0<10'), ('10<100', '10<100'), ('100<500', '100<500'), ('500<1k', '10k<50k'), ('50k<100k', '50k<100k'), ('100k<', '100k<')], max_length=50),
        ),
        migrations.AlterField(
            model_name='ecandidate',
            name='candidate_phone',
            field=models.IntegerField(blank=True),
        ),
    ]