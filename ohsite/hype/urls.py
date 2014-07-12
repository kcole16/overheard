from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^home/$', 'hype.views.home', name='hype_home'),
    url(r'^comments/(.+)$', 'hype.views.comments', name='hype_comments'),
    url(r'^add_comment/(.+)$', 'hype.views.add_comment', name='hype_add_comment'),
    url(r'^get_topics/$', 'hype.views.get_topics', name='hype_get_topics'),
)