from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = (
			'username', 
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2'
			)

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			match = User.objects.get(email=email)
		except User.DoesNotExist:
			return email

		raise forms.ValidationError("This email address is already in use.")

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			match = User.objects.get(username=username)
		except User.DoesNotExist:
			return username

		raise forms.ValidationError("This username is already in use.")

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']

		if commit:
			user.save()

		return user



class LoginForm(AuthenticationForm):
	username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
	password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))