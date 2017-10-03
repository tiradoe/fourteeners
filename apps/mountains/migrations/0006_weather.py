# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mountains', '0005_auto_20150329_2356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('day', models.IntegerField(default=0)),
                ('county', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('speed', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('temp', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('cloud', models.IntegerField(default=0)),
                ('humidity', models.IntegerField(default=0)),
                ('mountain', models.ForeignKey(default=None, to='mountains.Mountain')),
            ],
        ),
    ]
