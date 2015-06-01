#encoding=utf-8

from django.db import models
from django.utils import timezone
import os
# import sys
# reload(sys)
from django.template.defaultfilters import slugify
import markdown
from django.core.files.base import ContentFile

# sys.setdefaultencoding('utf8')


upload_dir = 'content/BlogPost/%s/%s'


class BlogPost(models.Model):

    def get_upload_md_name(self, filename):
        year = self.pub_date.year
        upload_to = upload_dir % (year, self.title + '.md')
        return upload_to

    def get_html_name(self, filename):
        year = self.pub_date.year
        upload_to = upload_dir % (year, filename)
        print "get html name %s"%upload_to
        return upload_to

    #id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    body = models.TextField(blank=True)
    md_file = models.FileField(upload_to=get_upload_md_name, blank=True)
    pub_date = models.DateTimeField('date published', default=timezone.now())
    last_edit_time = models.DateTimeField('last edited', default=timezone.now())
    category = models.CharField(max_length=30)
    tags = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200, blank=True)
    html_file = models.FileField(upload_to=get_html_name, blank=True)

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


        if self.body:
            self.body.encode(encoding='utf-8')
            r = markdown.markdown(self.body, ['codehilite'])
            # print "markdown :"%ContentFile(r)
            print r
            filename_t = self.title+".html"
            self.html_file.save(filename_t.encode('utf-8'), ContentFile(r), save=False)
            # print "after all html file %s"%self.html_file.path
            self.html_file.close()
        models.Model.save(self)


    def display_html(self):
        print "display html: %s"%self.html_file
        with open(self.html_file.path) as f:
        # with open(self.html_file.path, encoding='utf-8') as f:
            print "print display html"
            html_content = f.read()
            print html_content
            return html_content

