#encoding=utf-8

from django.shortcuts import render
from .models import BlogPost
import datetime
from collections import defaultdict
from django import forms
from models import User
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext

from blog_forms import BlogPublishForm
from models import *

from django.http import HttpResponseRedirect
from django.template import RequestContext

import hashlib

# Create your views here.

exclude_posts = ("about", "projects")

def test(request):
    args = dict()
    # return render(request, 'test.html', args)
    return render(request, 'test_boot3.html', args)


def home(request):
    print "view home"
    username = request.session.get('username', False)
    if username:
        print "home index page, username is %s" % username
    count = 3
    args = dict()
    args['blogposts'] = BlogPost.objects.exclude(title__in=exclude_posts).order_by('-pub_date')
    # return render(request, 'blog_base.html', args)
    # return render(request, 'test_boot3.html', args)
    return render(request, 'blog_home.html', args)


def blog_article(request, year, month, day, slug):
    print "enter blogpost new"
    value = datetime.datetime(int(year), int(month), int(day))
    print value

    entry = BlogPost.objects.filter(
        slug=slug,
        pub_date__range=(datetime.datetime.combine(value, datetime.time.min),
                         datetime.datetime.combine(value, datetime.time.max))
    )
    if not entry:
        # TODO raise 404
        # print "404"
        return render(request, 'blog_404.html')
    else:
        # print(""+ entry)
        args = {'blogpost': entry[0]}
        return render(request, 'blog_article.html', args)


def blog_archive(request):
    args = dict()
    blogposts = BlogPost.objects.exclude(title__in=exclude_posts)

    def get_sorted_posts():
        posts_by_year = defaultdict(list)
        for post in blogposts:
            year = post.pub_date.year
            posts_by_year[year].append(post)
        posts_by_year = sorted(posts_by_year.items(), reverse=True)
        return posts_by_year

    args['posts_by_year'] = get_sorted_posts()
    return render(request, 'blog_archive.html', args)


def blog_publish(request):
    args = dict()
    return render(request, 'publish_page/publish.html', args)

def blog_add(request):
    print "enter blog_add view func:"
    if request.method == 'POST':
        post_form = BlogPublishForm(request.POST)

        # if not post_form:
        # print "blog_add post is %s" % post_form
        if post_form.is_valid():
            print "post form is valid"
            clean_data = post_form.cleaned_data
            blog_title = clean_data['title']
            blog_content = clean_data['content']
            blog_category = clean_data['category']
            blog_status = clean_data['status']
            print "title is %s" % clean_data['title']
            print "content is %s" % clean_data['content']
            print "category is %s" % clean_data['category']
            print "status is %s" % blog_status
            save_blog(blog_title, blog_content, blog_category, blog_status)
        # if not post_form.title:
        #     print "blog title is %s" % post_form.title
        # elif not post_form.content:
        #     print "blog content is %s" % post_form.content
    form = BlogPublishForm()
    # return render(request, 'publish_page/pform.html', {'form': form})
    # return render(context_instance=RequestContext(request), 'publish_page/pform.html', {'form': form})
    # context_instance=RequestContext(req)
    return render_to_response('publish_page/pform.html', {'form': form}, context_instance=RequestContext(request))


def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            User.objects.create(username=username, password=password)
            return HttpResponse('register successful')
    else:
        uf = UserForm()
    return render_to_response('user/register.html', {'uf': uf}, context_instance=RequestContext(request))


def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 加密
            password_sha1 = hashlib.sha256(password).hexdigest()
            print "passwd sh1 is %s" % password_sha1
            # user = User.objects.filter(username=username, password=password)
            user = User.objects.filter(username=username, password=password_sha1)
            if user:
                print "%s login success " % username
                #登陆成功，跳转到主页
                response = HttpResponseRedirect('/blog/')
                #cookie 方式
                # resonse.set_cookie('username', username, 3600)
                #session方式
                request.session['username'] = username
                # 设置过期时间
                request.session.set_expiry(360)
                return response
            else:
                return HttpResponseRedirect('/blog/login')
    else:
        uf = UserForm()
    return render_to_response('user/login.html', {'uf': uf}, context_instance=RequestContext(request))


def logout(request):
    response = HttpResponse('logout')
    # cookie方式
    # response.delete_cookie('username')
    del request.session['username']
    return response


def login_index(request):
    username = request.COOKIES.get('username', '')
    return render_to_response('user/login_index.html', {'username': username})


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=50)
    password = forms.CharField(label='密码',  widget=forms.PasswordInput())


