from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^new$', views.new),
	url(r'^process$',views.process),
	url(r'^show/(?P<id>\d+)$', views.show),
	url(r'^edit/(?P<id>\d+)$', views.edit),
	url(r'^delete/(?P<id>\d+)$', views.delete),
	url(r'^update/(?P<id>\d+)$', views.update)
]