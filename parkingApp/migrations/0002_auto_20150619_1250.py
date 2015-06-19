# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkingApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='placemark',
            old_name='description',
            new_name='rate',
        ),
        migrations.AddField(
            model_name='placemark',
            name='credit_card',
            field=models.CharField(max_length=300, default=''),
        ),
        migrations.AddField(
            model_name='placemark',
            name='intersection',
            field=models.CharField(max_length=300, default=''),
        ),
        migrations.AddField(
            model_name='placemark',
            name='link',
            field=models.CharField(max_length=300, default=''),
        ),
        migrations.AddField(
            model_name='placemark',
            name='location',
            field=models.CharField(max_length=300, default=''),
        ),
        migrations.AddField(
            model_name='placemark',
            name='time',
            field=models.CharField(max_length=300, default=''),
        ),
    ]
