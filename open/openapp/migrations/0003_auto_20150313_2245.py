# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openapp', '0002_auto_20150311_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='rating',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
    ]
