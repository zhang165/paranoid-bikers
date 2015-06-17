# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkingApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Placemark',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('placemark', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('lat', models.DecimalField(decimal_places=14, max_digits=20)),
                ('lon', models.DecimalField(decimal_places=14, max_digits=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='parkingspot',
            name='location',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='ParkingSpot',
        ),
    ]
