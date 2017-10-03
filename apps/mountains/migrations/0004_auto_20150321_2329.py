# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mountains', '0003_auto_20150222_0703'),
    ]

    operations = [
        migrations.AddField(
            model_name='mountain',
            name='cloud_cover',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mountain',
            name='county',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='mountain',
            name='humidity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mountain',
            name='status',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='mountain',
            name='status_image',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='mountain',
            name='temperature',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=3),
        ),
        migrations.AddField(
            model_name='mountain',
            name='wind_speed',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=3),
        ),
    ]
