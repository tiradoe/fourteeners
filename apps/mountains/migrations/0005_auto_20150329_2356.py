# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mountains', '0004_auto_20150321_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mountain',
            name='cloud_cover',
        ),
        migrations.RemoveField(
            model_name='mountain',
            name='county',
        ),
        migrations.RemoveField(
            model_name='mountain',
            name='humidity',
        ),
        migrations.RemoveField(
            model_name='mountain',
            name='status',
        ),
        migrations.RemoveField(
            model_name='mountain',
            name='status_image',
        ),
        migrations.RemoveField(
            model_name='mountain',
            name='temperature',
        ),
        migrations.RemoveField(
            model_name='mountain',
            name='wind_speed',
        ),
    ]
