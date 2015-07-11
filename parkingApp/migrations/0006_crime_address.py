# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkingApp', '0005_auto_20150710_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='crime',
            name='address',
            field=models.CharField(max_length=300, default=''),
        ),
    ]
