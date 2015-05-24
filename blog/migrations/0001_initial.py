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
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField(blank=True)),
                ('md_file', models.FileField(upload_to=blog.models.get_upload_md_name, blank=True)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2015, 5, 9, 12, 58, 33, 610893, tzinfo=utc), verbose_name=b'date published')),
                ('last_edit_time', models.DateTimeField(default=datetime.datetime(2015, 5, 9, 12, 58, 33, 610929, tzinfo=utc), verbose_name=b'last edited')),
                ('category', models.CharField(max_length=30)),
                ('tags', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=200, blank=True)),
                ('html_file', models.FileField(upload_to=blog.models.get_html_name, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
                ('author', models.ManyToManyField(to='blog.Author')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(to='blog.Publisher'),
            preserve_default=True,
        ),
    ]
