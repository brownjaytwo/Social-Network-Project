from django.shortcuts import render, redirect, get_object_or_404

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

from posts.views import photo_post
from posts.views import post
from posts.views import youtube_post

from profiles.models import UserProfile
from profiles.forms import (
	EditProfileForm,
	EditUserProfile, 
	)

from friendship.models import Friend, Block, FriendshipRequest


# Create your views here.
def view_profile(request, pk=None):
	storage = messages.get_messages(request)
	if pk:
		user = User.objects.get(pk=pk)
	else:
		user = request.user
	
	# Code to post stuff from user profile
	form = HomeForm()
	post(request, form)

	# Code to post photo posts from user profile
	form_photo = PhotoPostForm()
	photo_post(request, form_photo)

	form_youtube = YoutubePostForm()
	youtube_post(request, form_youtube)

	posts = Post.objects.filter(user=user).order_by('-created')
	photo_posts = PhotoPost.objects.filter(user=user).order_by('-created')
	youtube_posts = YoutubePost.objects.filter(user=user).order_by('-created')
	# print(photo_posts)

	friends_pk = Friend.objects.friends(user)
	friends_user = Friend.objects.friends(request.user)

	sent_requests = FriendshipRequest.objects.select_related("from_user", "to_user").filter(from_user=request.user).values_list('to_user_id', flat=True)
	received_requests = FriendshipRequest.objects.select_related("from_user", "to_user").filter(to_user=request.user).values_list('from_user', flat=True)

	args = {'user': user, 
			'message': storage, 
			'form': form, 
			'form_photo': form_photo, 
			'form_youtube': form_youtube, 
			'posts': posts, 
			'photo_posts': photo_posts,
			'youtube_posts': youtube_posts,
			'friends_pk': friends_pk, 
			'friends_user': friends_user, 
			"sent_requests": sent_requests, 
			"received_requests": received_requests
			}
	return render(request, 'profiles/profile.html', args)


def view_profile_photos(request):
	form_photo = PhotoPostForm()
	photo_post(request, form_photo)
	
	args = {'form_photo': form_photo}
	return render(request, 'profiles/profile_photos.html', args)


def edit_profile(request):
	if request.method == 'POST':
		form_EPF = EditProfileForm(request.POST, instance=request.user)
		form_EUP = EditUserProfile(request.POST, request.FILES, instance=request.user.userprofile)
		

		if form_EPF.is_valid() and form_EUP.is_valid():
			form_EPF.save()
			form_EUP.save()
			return redirect(reverse('profiles:view_profile'))

	else:
		form_EPF = EditProfileForm(instance=request.user)
		form_EUP = EditUserProfile(instance=request.user.userprofile)

		args = {'form_EPF': form_EPF, "form_EUP": form_EUP}
		return render(request, 'profiles/edit_profile.html', args)
