from django.conf.urls import patterns, include, url

from django.contrib import admin
from libmgmt.api import AuthorResource

author_resource = AuthorResource() 
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^polls/', include('polls.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^libr/', include('libmgmt.urls')),
	url(r'^api/', include(author_resource.urls))
)