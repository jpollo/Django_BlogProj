# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150823_0806'),
    ]

    operations = [
        migrations.AddField(
            model_name='simpleblogpost',
            name='html_file',
            field=models.FileField(upload_to=b'simple_blog_dir', blank=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='last_edit_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 23, 8, 37, 33, 996635, tzinfo=utc), verbose_name=b'last edited'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 23, 8, 37, 33, 996589, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
