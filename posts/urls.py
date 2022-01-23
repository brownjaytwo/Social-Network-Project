from django.urls import re_path, path
from . import views

app_name = 'posts'
urlpatterns = [
	re_path(r'^view_photo/(?P<pk>\d+)/$', views.photo_detail, name='photo_detail'),
	re_path(r'^delete-post/(?P<pk>\d+)/$', views.post_delete, name='post_delete'),
	re_path(r'^delete-photo/(?P<pk>\d+)/$', views.photo_delete, name='photo_delete'),
]