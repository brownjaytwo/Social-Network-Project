from django import forms
from posts.models import Post
from posts.models import PhotoPost
from posts.models import YoutubePost

class HomeForm(forms.ModelForm):
	post = forms.CharField(widget=forms.Textarea(
		attrs={
		'maxlength': '500',
		'class': 'form-control',
		'placeholder': 'Write a post...',
		'autocomplete': 'off',
		'rows': '2'
		}
	))

	class Meta:
		model = Post
		fields = ('post',)

class PhotoPostForm(forms.ModelForm):
	caption = forms.CharField(widget=forms.Textarea(
		attrs={
		'maxlength': '500',
		'class': 'form-control',
		'placeholder': 'Write a caption for this photo...',
		'autocomplete': 'off',
		'rows': '2'
		}
	))

	class Meta:
		model = PhotoPost
		fields = ('image', 'caption')


class YoutubePostForm(forms.ModelForm):
	link = forms.CharField(widget=forms.Textarea(
		attrs={
		'maxlength': '50',
		'class': 'form-control',
		'placeholder': 'Paste a youtube link here...',
		'autocomplete': 'off',
		'rows': '1'
		}
	))

	caption = forms.CharField(widget=forms.Textarea(
		attrs={
		'maxlength': '500',
		'class': 'form-control',
		'placeholder': 'Write a caption for this video...',
		'autocomplete': 'off',
		'rows': '2'
		}
	))
	class Meta:
		model = YoutubePost
		fields = ('link', 'caption')

