# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-20 06:01
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_image'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                ('stockholm', django.db.models.manager.Manager()),
            ],
        ),
    ]
