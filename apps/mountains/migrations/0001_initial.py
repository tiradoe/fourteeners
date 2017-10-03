# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mountain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('elevation', models.PositiveIntegerField(default=0)),
                ('difficulty', models.CharField(max_length=20)),
                ('lat', models.DecimalField(max_digits=7, decimal_places=4)),
                ('long', models.DecimalField(max_digits=7, decimal_places=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
