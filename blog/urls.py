__author__ = 'jpollo'


from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoDJ.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url('^$', views.test),
    url('^$', views.home),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', views.blog_article),
    url('^archive/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', views.blog_article),
)
