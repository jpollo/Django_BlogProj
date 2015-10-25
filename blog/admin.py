#encoding=utf-8

from django.contrib import admin

# Register your models here.

from blog.models import BlogPost
from blog.models import Category
from blog.models import SimpleBlogPost

#注册模块
admin.site.register(BlogPost)
admin.site.register(Category)
admin.site.register(SimpleBlogPost)
