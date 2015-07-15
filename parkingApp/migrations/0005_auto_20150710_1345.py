# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkingApp', '0004_crime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crime',
            name='description',
            field=models.CharField(default='', max_length=300),
        ),
    ]
