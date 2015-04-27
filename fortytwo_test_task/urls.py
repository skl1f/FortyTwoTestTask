from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'hello.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^requests/$', 'hello.views.requests', name='requests'),
    url(r'^edit/$', 'hello.views.edit_contacts', name='edit_contacts'),
    url(r'^api/contacts/$', 'hello.views.api_contacts', name='api_contacts'),
    url(r'^api/requests/$', 'hello.views.api_requests', name='api_requests'),
)

urlpatterns += patterns('',
                        url(r'^static/(?P<path>.*)$',
                            'django.views.static.serve',
                            {'document_root': settings.STATIC_ROOT}),)
