# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='latitude',
            field=models.CharField(max_length=200, default=datetime.datetime(2015, 8, 28, 1, 7, 4, 507069, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='film',
            name='longitude',
            field=models.CharField(max_length=200, default=datetime.datetime(2015, 8, 28, 1, 7, 20, 821824, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
