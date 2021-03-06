__author__ = 'jpollo'


from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns(
    '',
    url('^$', views.home),
    url('^archive/$', views.blog_archive),
    url('^publish/$', views.blog_publish),
    url('^add/$', views.blog_add),
    url('^register/$', views.register),
    url('^login/$', views.login),

    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', views.blog_article),
    url('^archive/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', views.blog_article),
)
