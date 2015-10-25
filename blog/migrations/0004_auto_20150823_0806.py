# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150823_0323'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleBlogPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField(blank=True)),
                ('category', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='last_edit_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 23, 8, 6, 2, 233501, tzinfo=utc), verbose_name=b'last edited'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 23, 8, 6, 2, 233459, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
