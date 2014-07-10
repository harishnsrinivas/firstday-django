from django.conf.urls import patterns, url
from libmgmt import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name="index"),
	url(r'^searchbook/$', views.searchbook, name="search"),
	url(r'^book/(?P<book_id>\d+)/$', views.bookdetail, name="bookdetail"),
	url(r'^book/(?P<book_id>\d+)/rent/$', views.rentbook, name="rentbook"),
	url(r'^book/(?P<book_id>\d+)/return/$', views.returnbook, name="returnbook"),
) 