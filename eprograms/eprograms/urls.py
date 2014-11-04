from django.conf.urls import patterns, include, url
from django.contrib import admin
from eduprograms.api import router

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),

    # include api links
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
)
