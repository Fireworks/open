from django.conf.urls import patterns, include, url
from django.contrib import admin
import openapp.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'open.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(openapp.urls)),
)
