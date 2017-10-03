# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mountains', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Climb',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('mountain', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('summit_date', models.DateField()),
                ('summit_time', models.TimeField()),
                ('finish_date', models.DateField()),
                ('finish_time', models.TimeField()),
                ('total_distance', models.PositiveIntegerField()),
                ('notes', models.TextField()),
                ('climber_id', models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
