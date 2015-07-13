# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkingApp', '0007_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='LowCrimePlacemark',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('placemark_id', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('rate', models.CharField(max_length=300, default='')),
                ('credit_card', models.CharField(max_length=300, default='')),
                ('location', models.CharField(max_length=300, default='')),
                ('intersection', models.CharField(max_length=300, default='')),
                ('time', models.CharField(max_length=300, default='')),
                ('link', models.CharField(max_length=300, default='')),
                ('lat', models.DecimalField(max_digits=20, decimal_places=14)),
                ('lon', models.DecimalField(max_digits=20, decimal_places=14)),
            ],
        ),
        migrations.DeleteModel(
            name='BikeTheft',
        ),
    ]
