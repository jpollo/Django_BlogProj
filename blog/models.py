#encoding=utf-8

from django.db import models
from django.utils import timezone
import os
# import sys
# reload(sys)
from django.template.defaultfilters import slugify
import markdown
from django.core.files.base import ContentFile
from django import forms

# sys.setdefaultencoding('utf8')

upload_dir = 'content/BlogPost/%s/%s'


def get_upload_md_name(obj, filename):
    year = obj.pub_date.year
    upload_to = upload_dir % (year, obj.title + '.md')
    return upload_to


def get_html_name(obj, filename):
    print "enter func get html name"
    year = obj.pub_date.year
    upload_to = upload_dir % (year, filename)
    # print "get html name %s
    return upload_to


class BlogPost(models.Model):

    STATUS = (('DRAFT', 'draft'), ('PUBLISHED', 'published'))

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    body = models.TextField(blank=True)
    md_file = models.FileField(upload_to=get_upload_md_name, blank=True)
    pub_date = models.DateTimeField('date published', default=timezone.now())
    last_edit_time = models.DateTimeField('last edited', default=timezone.now())
    category = models.CharField(max_length=30)
    tags = models.CharField(max_length=20)
    # tags forms.MultiValueField
    slug = models.SlugField(max_length=200, blank=True, editable=False)
    html_file = models.FileField(upload_to=get_html_name, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default=STATUS[0][0])

    def filename(self):
        if self.md_file:
            return os.path.basename(self.title)
        else:
            return 'no md file'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        print ("save action")
        self.title = unicode(self.title).decode(encoding='utf-8')
        self.slug = slugify(unicode(self.title.replace('-', 'and')))

        if not self.body and self.md_file:
            self.body = self.md_file.read()
            print "read md file content to body"

        if self.body:
            print "body is not null"
            self.body.encode(encoding='utf-8')
            print "before markdown"
            r = markdown.markdown(self.body, ['codehilite'])
            print "after markdown"
            # print "markdown :"%ContentFile(r)
            print r
            print "after print markdown content"
            filename_t = self.title+".html"
            self.html_file.save(filename_t.encode('utf-8'), ContentFile(r), save=False)
            # print "after all html file %s"%self.html_file.path
            self.html_file.close()
            print "html file close"
        models.Model.save(self)

    def display_html(self):
        print "display html: %s"%self.html_file
        with open(self.html_file.path) as f:
            html_content = f.read()
            return html_content

    def get_absolute_url(self):
        print("enter func get url")
        print self.slug
        print ("exit func get url")
        return "%s%s" % (self.pub_date.strftime("%Y/%m/%d/"), self.slug)

    def getcategory(self):
        return self.category

    def gettags(self):
        return self.tags

    def __str__(self):
        # print "BlogBost"
        return self.title


class SimpleBlogPost(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    category = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    html_file = models.FileField(upload_to='simple_blog_dir', blank=True)
    pub_date = models.DateTimeField('date published', default=timezone.now())
    last_edit_date = models.DateTimeField('date last edit', default=timezone.now())

    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.username


class Category(models.Model):
    category_code = models.CharField(max_length=50)
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_code


def save_blog(blog_title, blog_content, blog_category, blog_status):
    print "enter save blog"
    try:
        print "filter blog by title %s" % blog_title
        found = SimpleBlogPost.objects.get(title=blog_title)
        if found:
            update_blog(blog_title, blog_content, blog_category, blog_status)
        else:
            print "can not find simple blog"
    except SimpleBlogPost.DoesNotExist:
        print "not found with post title, so add this blog"
        add_blog(blog_title, blog_content, blog_category, blog_status)

    # blog = SimpleBlogPost(title=blog_title, content=blog_content, category=blog_category, status=blog_status)
    # blog.save()
    # if blog_content:
    #     r = markdown.markdown(blog_content, ['codehilite'])
    #     filename = blog_title + ".html"
    #     blog.html_file.save(filename, ContentFile(r), save=True)
    #     blog.html_file.close()

    print "exit save blog"


def add_blog(blog_title, blog_content, blog_category, blog_status):
    print "add a post blog"
    blog = SimpleBlogPost(title=blog_title, content=blog_content, category=blog_category, status=blog_status)
    blog.save()
    if blog_content:
        r = markdown.markdown(blog_content, ['codehilite'])
        filename = blog_title + ".html"
        blog.html_file.save(filename, ContentFile(r), save=True)
        blog.html_file.close()


def update_blog(blog_title, blog_content, blog_category, blog_status):
    print "update a post blog"






