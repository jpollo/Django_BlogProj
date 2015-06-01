from django.shortcuts import render
from .models import BlogPost

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
    return render(request, 'test_boot3.html', args)