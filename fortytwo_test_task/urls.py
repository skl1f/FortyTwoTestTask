from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'hello.views.home', name='home'),
    url(r'^requests/', 'hello.views.requests', name='requests'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/requests', 'hello.views.api_requests', name='api_requests')
)

urlpatterns += patterns('',
                        url(r'^static/(?P<path>.*)$',
                            'django.views.static.serve',
                            {'document_root': settings.STATIC_ROOT}),)
