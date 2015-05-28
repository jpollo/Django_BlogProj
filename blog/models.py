#encoding=utf-8

from django.db import models
from django.utils import timezone


upload_dir = 'content/BlogPost/%s/%s'


def get_upload_md_name(self, filename):
    year = self.pub_date.year
    upload_to = upload_dir % (year, self.title + '.md')
    return upload_to


def get_html_name(self, filename):
    year = self.pub_date.year
    upload_to = upload_dir % (year, filename)
    return upload_to


class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    body = models.TextField(blank=True)
    md_file = models.FileField(upload_to=get_upload_md_name, blank=True)
    pub_date = models.DateTimeField('date published', default=timezone.now())
    last_edit_time = models.DateTimeField('last edited', default=timezone.now())
    category = models.CharField(max_length=30)
    tags = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200, blank=True)
    html_file = models.FileField(upload_to=get_html_name, blank=True)

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50, blank = True)  # blank为True表明可空

class Author(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()


class BlogCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=20)
    blog_id = models.CharField(max_length=30)

