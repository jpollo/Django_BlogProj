#encoding=utf-8

from django.contrib import admin

# Register your models here.

from blog.models import BlogPost

#注册模块
admin.site.register(BlogPost)
