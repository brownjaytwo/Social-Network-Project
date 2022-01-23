from django.urls import re_path, path
from . import views
from accounts.forms import LoginForm
from django.contrib.auth.views import (
	login, 
	logout, 
	password_reset, 
	password_reset_done,
	password_reset_confirm,
	password_reset_complete,
	)

app_name = 'people'
urlpatterns = [
	re_path(r'^all/$', views.view_people_all, name='view_people_all'),
	re_path(r'^blocked/$', views.view_people_blocked, name='view_people_blocked'),
	re_path(r'^requests/$', views.view_people_requests, name='view_people_requests'),
	re_path(r'^friends/$', views.view_people_friends, name='view_people_friends'),

	re_path(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends'),
	re_path(r'^request/(?P<operation>.+)/(?P<pk>\d+)/$', views.request_response, name='request_response'),
]