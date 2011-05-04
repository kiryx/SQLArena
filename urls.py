from django.conf.urls.defaults import patterns, include, url
import os.path
from django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SQLArena.views.home', name='home'),
    # url(r'^SQLArena/', include('SQLArena.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
#	(r'^admin/', include('django.contrib.admin.urls')),
#	(r'^/?$', direct_to_template, {
#        'template': 'list.html'
#    })
    # Uncomment the next line to enable the admin:
    (r'', 'sprawdzarka.views.index'),
    (r'^admin/', include(admin.site.urls)),
)
