# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import blog.models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField(blank=True)),
                ('md_file', models.FileField(upload_to=blog.models.get_upload_md_name, blank=True)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2015, 6, 6, 5, 4, 44, 752007, tzinfo=utc), verbose_name=b'date published')),
                ('last_edit_time', models.DateTimeField(default=datetime.datetime(2015, 6, 6, 5, 4, 44, 752053, tzinfo=utc), verbose_name=b'last edited')),
                ('category', models.CharField(max_length=30)),
                ('tags', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=200, editable=False, blank=True)),
                ('html_file', models.FileField(upload_to=blog.models.get_html_name, blank=True)),
                ('status', models.CharField(default=b'DRAFT', max_length=10, choices=[(b'DRAFT', b'draft'), (b'PUBLISHED', b'published')])),
            ],
        ),
    ]
