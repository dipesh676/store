# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SalesDescription', '0002_auto_20171006_2200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AlterField(
            model_name='product',
            name='productID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
