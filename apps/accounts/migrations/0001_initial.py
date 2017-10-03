# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('birthday', models.DateField()),
                ('location', models.CharField(max_length=255)),
                ('picture', models.ImageField(blank=True, upload_to='media', default=None)),
                ('next_mountain1', models.CharField(max_length=50)),
                ('next_mountain2', models.CharField(max_length=50)),
                ('next_mountain3', models.CharField(max_length=50)),
                ('next_mountain4', models.CharField(max_length=50)),
                ('next_mountain5', models.CharField(max_length=50)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
