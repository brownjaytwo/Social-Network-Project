from django.urls import re_path, path
from home.views import home
from . import views

app_name = 'home'
urlpatterns = [
	re_path(r'^$', views.home, name='home'),
]