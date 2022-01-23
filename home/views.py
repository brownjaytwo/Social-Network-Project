from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Q
from friendship.models import Friend, Block, FriendshipRequest

from posts.forms import HomeForm
from posts.forms import PhotoPostForm
from posts.models import Post
from posts.models import PhotoPost
from posts.views import post
from posts.views import photo_post

from itertools import chain

from accounts.views import photo_post
from people.views import pk_to_user


template_name = 'home/home.html'

def home(request):
	form = HomeForm()
	post(request, form)

	form_photo = PhotoPostForm()
	photo_post(request, form_photo)

	friends = Friend.objects.friends(request.user)
	sent_requests = FriendshipRequest.objects.select_related("from_user", "to_user").filter(from_user=request.user).values_list('to_user_id', flat=True)

	posts = Post.objects.filter(Q(user__in=friends) | Q(user=request.user)).order_by('-created')
	photo_posts = PhotoPost.objects.filter(Q(user__in=friends) | Q(user=request.user)).order_by('-created')

	all_posts = list(chain(posts, photo_posts))
	# print("All post ids: {0}".format(all_posts))

	users = User.objects.exclude(id=request.user.id)
	
	received_requests = pk_to_user(request, "received_requests")

	args = {'form': form, 'form_photo': form_photo, 'posts': posts, 'users': users, 'friends': friends, 'sent_requests': sent_requests, 'received_requests': received_requests}
	return render(request, template_name, args)
