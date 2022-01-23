from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from profiles.models import UserProfile

class EditProfileForm(UserChangeForm):

	class Meta:
		model = User
		fields = (
			'email',
			'first_name',
			'last_name',
			'password',
			)

class EditUserProfile(ModelForm):
	description = forms.CharField(required=False)
	city = forms.CharField(required=False)
	website = forms.URLField(required=False)

	class Meta:
		model = UserProfile
		fields = (
			'description',
			'city',
			'website',
			'avatar',
			)