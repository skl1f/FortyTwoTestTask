from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    url(r'^$', 'hello.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
                        url(r'^static/(?P<path>.*)$',
                            'django.views.static.serve',
                            {'document_root': settings.STATIC_ROOT}),)
