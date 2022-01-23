from urllib.parse import urlparse, parse_qs

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.core.exceptions import ValidationError

from posts.forms import HomeForm
from posts.forms import PhotoPostForm
from posts.forms import YoutubePostForm

from posts.models import Post
from posts.models import PhotoPost
from posts.models import YoutubePost

# Create your views here.
template_name = 'home/home.html'

def post(request, form):
	form = HomeForm(request.POST)
	if form.is_valid():
		post = form.save(commit=False)
		post.user = request.user
		post.save()
		text = form.cleaned_data['post']
		form = HomeForm()
		return redirect('home:home')

	args = {'form': form}
	return render(request, template_name, args)

def post_delete(request, pk):
	post = Post.objects.get(pk=pk)
	if request.user.id == post.user.id:
		post.delete()
	return redirect('home:home')

def photo_post(request, form_photo):
	form_photo = PhotoPostForm(request.POST, request.FILES)
	if form_photo.is_valid():
		post = form_photo.save(commit=False)
		post.user = request.user
		post.save()
		form_photo = PhotoPostForm()
		return redirect('profiles:view_profile')
	else:
		form_photo = PhotoPostForm()

def photo_detail(request, pk):
	photo = PhotoPost.objects.get(pk=pk)

	args = {'photo': photo}
	return render(request, 'profiles/photo_detail.html', args)

def photo_delete(request, pk):
	photo = PhotoPost.objects.get(pk=pk)
	if request.user.id == photo.user.id:
		photo.delete()
	return redirect('home:home')

def youtube_post(request, form_video):
	form_video = YoutubePostForm(request.POST)
	raw_link = form_video['link'].value()

	if form_video.is_valid():
		query = urlparse(raw_link)
		if query.hostname == 'youtu.be':
			video_id = query.path[1:]
			print(video_id)
		elif query.hostname in ('www.youtube.com', 'youtube.com'):
			if query.path == '/watch':
				p = parse_qs(query.query)
				video_id = p['v'][0]
				print(video_id)
			elif query.path[:7] == '/embed/':
				video_id = query.path.split('/')[2]
				print(video_id)
			elif query.path[:3] == '/v/':
				video_id = query.path.split('/')[2]
				print(video_id)


		else:
			print("Please enter a youtube link")
			return messages.error(request, "Error: Please submit a valid youtube link")

		youtube_post = form_video.save(commit=False)
		youtube_post.link = video_id
		youtube_post.user = request.user
		youtube_post.save()
		form = YoutubePostForm()
		return redirect('home:home') 