# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 08:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feedbacks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='write_to',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='received', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
