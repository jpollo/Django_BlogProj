# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150823_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='simpleblogpost',
            name='last_edit_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 25, 7, 41, 27, 697243, tzinfo=utc), verbose_name=b'date last edit'),
        ),
        migrations.AddField(
            model_name='simpleblogpost',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 25, 7, 41, 27, 697203, tzinfo=utc), verbose_name=b'date published'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='last_edit_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 25, 7, 41, 27, 695955, tzinfo=utc), verbose_name=b'last edited'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 25, 7, 41, 27, 695899, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
