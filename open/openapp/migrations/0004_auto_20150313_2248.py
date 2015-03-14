# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openapp', '0003_auto_20150313_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='rating',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
