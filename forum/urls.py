from django.conf.urls import patterns, include, url
from posts.views import users_view

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'forum.views.home', name='home'),
    # url(r'^forum/', include('forum.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', users_view.new),
    url(r'^posts/', include('posts.urls')),
    url(r'^users/new/$', users_view.new),
    url(r'^users/login/$', users_view.login),
    url(r'^users/logout/$', users_view.logout),
    url(r'^users/register/$', users_view.register),
    url(r'^users/change_password/$', users_view.change_password),
    url(r'^users/reset_password/$', users_view.reset_password),
)
