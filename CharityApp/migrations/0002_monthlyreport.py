# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-17 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CharityApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('pets_resqued', models.IntegerField()),
                ('money_spent', models.IntegerField()),
                ('spends', models.TextField()),
            ],
        ),
    ]