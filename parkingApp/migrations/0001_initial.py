# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ParkingSpot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=120)),
                ('toll', models.DecimalField(decimal_places=2, max_digits=4)),
                ('location', models.OneToOneField(to='parkingApp.Location')),
            ],
        ),
    ]
