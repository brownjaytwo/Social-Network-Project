from django.shortcuts import render, redirect, get_object_or_404
from accounts.forms import RegistrationForm 

from django.urls import reverse, resolve
from django.http import HttpResponse, HttpRequest
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.contrib.auth.decorators import login_required

from posts.forms import HomeForm
from posts.forms import PhotoPostForm
from posts.forms import YoutubePostForm

from posts.models import Post
from posts.models import PhotoPost
from posts.models import YoutubePost

from profiles.models import UserProfile
from friendship.models import Friend, Block, FriendshipRequest

from posts.views import photo_post
from posts.views import post
from posts.views import youtube_post

# Create your views here.

def register(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			# Fix unique email bug
			user = form.save()
			
			# Logs in newly registered
			username = request.POST.get('username')
			password = request.POST.get('password1')
			login(request, user)
			return redirect(reverse('home:home'))
	else:
		form = RegistrationForm()

	args = {'form': form}
	return render(request, 'accounts/reg_form.html', args)


def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			messages.success(request, 'Your new password has been saved.')
			update_session_auth_hash(request, form.user)
			return redirect(reverse('profiles:view_profile'))

	else:
		form = PasswordChangeForm(user=request.user)

	args = {'form': form}
	return render(request, 'accounts/change_password.html', args)

