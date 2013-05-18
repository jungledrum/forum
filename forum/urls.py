from django.conf.urls import patterns, include, url
from users.views import users_view

urlpatterns = patterns('',
    url(r'^$', users_view.new),
    url(r'^posts/', include('posts.urls')),
    url(r'^users/new/$', users_view.new),
    url(r'^users/login/$', users_view.login),
    url(r'^users/logout/$', users_view.logout),
    url(r'^users/register/$', users_view.register),
)
