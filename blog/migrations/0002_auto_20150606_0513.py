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
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 5, 13, 25, 429254, tzinfo=utc), verbose_name=b'last edited'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 5, 13, 25, 429180, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
