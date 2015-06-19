# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkingApp', '0002_auto_20150619_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placemark',
            name='rate',
            field=models.CharField(max_length=300, default=''),
        ),
    ]
