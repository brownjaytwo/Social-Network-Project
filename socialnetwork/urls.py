from django.urls import re_path, path, include
from django.contrib import admin
from socialnetwork import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	re_path(r'^$', views.login_redirect, name='login_redirect'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^account/', include('accounts.urls')),
    re_path(r'^friendship/', include('friendship.urls')),
    re_path(r'^home/', include('home.urls')),
    re_path(r'^people/', include('people.urls')),
    re_path(r'^posts/', include('posts.urls')),
    re_path(r'^profiles/', include('profiles.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
