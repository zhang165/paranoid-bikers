# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Placemark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('placemark_id', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('lat', models.DecimalField(max_digits=20, decimal_places=14)),
                ('lon', models.DecimalField(max_digits=20, decimal_places=14)),
            ],
        ),
    ]
