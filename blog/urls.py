__author__ = 'jpollo'


from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoDJ.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url('^$', views.test),
    url('^$', views.home),
)
