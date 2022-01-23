from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse, resolve
from django.http import HttpResponse, HttpRequest
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from profiles.models import UserProfile
from friendship.models import Friend, Block, FriendshipRequest


def pk_to_user(request, pk_list):

	received_requests = FriendshipRequest.objects.select_related("from_user", "to_user").filter(to_user=request.user).values_list('from_user', flat=True)
	sent_requests = FriendshipRequest.objects.select_related("from_user", "to_user").filter(from_user=request.user).values_list('to_user_id', flat=True)

	if pk_list == "received_requests":
		chosen_list = received_requests
	elif pk_list == "sent_requests":
		chosen_list = sent_requests

	# Gets user information from pk
	user_list = []
	for pk in chosen_list:
		user_obj = User.objects.get(pk=pk)
		user_list.append(user_obj)
	return user_list



def view_people_all(request):
	users = User.objects.all()
	friends = Friend.objects.friends(request.user)

	received_requests = FriendshipRequest.objects.select_related("from_user", "to_user").filter(to_user=request.user).values_list('from_user', flat=True)
	sent_requests = FriendshipRequest.objects.select_related("from_user", "to_user").filter(from_user=request.user).values_list('to_user_id', flat=True)

	list_title = "All Users"
	args = {'users': users, "list_title": list_title, 'friends': friends, 'sent_requests': sent_requests, "received_requests": received_requests}
	return render(request, 'people/people.html', args)


def view_people_friends(request):
	users = Friend.objects.friends(request.user)
	
	# testing user's friends output
	print(users)

	list_title = "Your friends"
	args = {'users': users, "list_title": list_title}
	return render(request, 'people/people.html', args)

def view_people_blocked(request):
	users = Block.objects.blocking(request.user)
	list_title = "Blocked Users"
	args = {'users': users, "list_title": list_title}
	return render(request, 'people/people.html', args)

def view_people_requests(request):
	# Needs to be fed through pk_to_user function to get user info from pk
	users = pk_to_user(request, "received_requests")

	list_title = "Friend Requests"
	args = {'users': users, "list_title": list_title}
	return render(request, 'people/people.html', args)


def change_friends(request, operation, pk):
	other_user = User.objects.get(pk=pk)
	current_url = request.get_full_path()

	if operation == 'add':
		Friend.objects.add_friend(request.user, other_user)
	elif operation == 'remove':
		Friend.objects.remove_friend(request.user, other_user)

	if current_url == 'all/':
		return redirect('people:view_people_all')
	elif current_url == 'people/friends':
		return redirect('people:view_people_friends')
	else:
		return redirect('home:home')


def request_response(request, operation, pk):
	if operation == 'accept':
		friend_request = FriendshipRequest.objects.get(from_user=pk, to_user=request.user)
		friend_request.accept()
	elif operation == 'reject':
		friend_request = FriendshipRequest.objects.get(from_user=pk, to_user=request.user)
		# friend_request.reject() doesn't do anything so this is the workaround
		friend_request.cancel()
	elif operation == 'cancel':
		friend_request = FriendshipRequest.objects.get(from_user=request.user, to_user=pk)
		friend_request.cancel()

	return redirect('people:view_people_requests')


