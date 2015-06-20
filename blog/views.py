from django.shortcuts import render
from .models import BlogPost
import datetime
from collections import defaultdict

# Create your views here.

exclude_posts = ("about", "projects")

def test(request):
    args = dict()
    # return render(request, 'test.html', args)
    return render(request, 'test_boot3.html', args)


def home(request):
    print "view home"
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
        print "404"
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