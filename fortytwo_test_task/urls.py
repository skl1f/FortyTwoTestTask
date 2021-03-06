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
    url(r'^api/requests/$', 'hello.views.api_requests', name='api_requests'),
    url(r'^api/counter/$', 'hello.views.api_requests_counter',
        name='api_requests_counter'),
)

urlpatterns += patterns('',
                        url(r'^uploads/(?P<path>.*)$',
                            'django.views.static.serve',
                            {'document_root': settings.MEDIA_ROOT}),
                        url(r'^static/(?P<path>.*)$',
                            'django.views.static.serve',
                            {'document_root': settings.STATIC_ROOT}),)
