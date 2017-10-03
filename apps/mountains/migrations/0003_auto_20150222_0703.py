# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mountains', '0002_climb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='climb',
            old_name='climber_id',
            new_name='climber',
        ),
    ]
