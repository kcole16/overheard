from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'core.views.home', name='home'),

    url(r'^around/', include('around.urls')),

    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout', 'core.views.logout_view', name='logout'),
)
