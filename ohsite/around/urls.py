from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^home/$', 'core.views.home', name='around_home'),
	url(r'^create_account/$', 'around.views.create_account', name='around_create_account'),
    url(r'^create_post/$', 'around.views.create_post', name='around_create_post'),
    url(r'^comments/(.+)$', 'around.views.comments', name='around_comments'),
    url(r'^add_comment/(.+)$', 'around.views.add_comment', name='around_add_comment'),
)