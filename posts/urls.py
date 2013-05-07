from django.conf.urls import patterns, url

from posts.views import posts_view, comments_view

urlpatterns = patterns('',
    url(r'^$', posts_view.index),
    url(r'^create/$', posts_view.create),
    url(r'^(?P<post_id>\w+)/comments/create/$', comments_view.create),
    url(r'^(?P<post_id>\w+)/comments/(?P<comment_id>\w+)/destroy/$', comments_view.destroy),
    url(r'^(?P<post_id>\w+)/destroy/$', posts_view.destroy),
    url(r'^page/(?P<page>\d+)/$', posts_view.index),
    url(r'^(?P<post_id>\w+)/$', posts_view.show),
    url(r'^(?P<post_id>\w+)/page/(?P<page>\d+)$', posts_view.show),
)
