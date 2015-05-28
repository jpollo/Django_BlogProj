# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='last_edit_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 24, 14, 5, 48, 340704, tzinfo=utc), verbose_name=b'last edited'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 24, 14, 5, 48, 340636, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
