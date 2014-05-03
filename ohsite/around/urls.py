from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	#url(r'^create_user/$', 'around.views.create_user', name='around_create_user'),
    url(r'^create_post/$', 'around.views.create_post', name='around_create_post'),
    url(r'^comments/(.+)$', 'around.views.comments', name='around_comments'),
    url(r'^add_comment/(.+)$', 'around.views.add_comment', name='around_add_comment'),
)