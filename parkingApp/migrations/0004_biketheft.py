# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkingApp', '0003_auto_20150619_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='BikeTheft',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('district', models.IntegerField(default=0)),
                ('Weekday', models.IntegerField(default=0)),
                ('Month', models.CharField(max_length=300, default='')),
                ('Year', models.IntegerField(default=0)),
                ('Block', models.CharField(max_length=300, default='')),
                ('BlockCleaned', models.CharField(max_length=300, default='')),
                ('AddressConsolidated', models.CharField(max_length=300, default='')),
                ('lat', models.DecimalField(decimal_places=14, max_digits=20)),
                ('lon', models.DecimalField(decimal_places=14, max_digits=20)),
            ],
        ),
    ]
