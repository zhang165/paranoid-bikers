# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkingApp', '0003_auto_20150619_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=300)),
                ('lat', models.DecimalField(max_digits=20, decimal_places=14)),
                ('lon', models.DecimalField(max_digits=20, decimal_places=14)),
            ],
        ),
    ]
