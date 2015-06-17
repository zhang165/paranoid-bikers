# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkingApp', '0002_auto_20150617_1231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='placemark',
            old_name='placemark',
            new_name='placemark_id',
        ),
    ]
