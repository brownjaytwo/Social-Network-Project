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

app_name = 'profiles'
urlpatterns = [
	re_path(r'^profile/$', views.view_profile, name='view_profile'),
	re_path(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
	re_path(r'^profile/friends/(?P<pk>\d+)/$', views.view_profile, name='view_profile_friends_with_pk'),
	re_path(r'^profile/photos/(?P<pk>\d+)/$', views.view_profile, name='view_profile_photos_with_pk'),
	re_path(r'^profile/videos/(?P<pk>\d+)/$', views.view_profile, name='view_profile_videos_with_pk'),
	re_path(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
]