# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openapp', '0002_auto_20150210_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='version',
            field=models.CharField(max_length=10, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='middle_name',
            field=models.CharField(default='TEST', max_length=20, blank=True),
            preserve_default=False,
        ),
    ]
