from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Transpose, SmartResize

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	description = models.CharField(max_length=100, default='')
	city = models.CharField(max_length=100, default='')
	website = models.URLField(default='')
	phone = models.IntegerField(default=0)
	
	avatar = models.ImageField(upload_to='profile_image', blank=True)
	avatar_profile = ImageSpecField(source='avatar', processors=[Transpose(),ResizeToFill(165, 165)], format='JPEG', options={'quality': 100})
	avatar_post = ImageSpecField(source='avatar', processors=[Transpose(),ResizeToFill(65, 65)], format='JPEG', options={'quality': 90})
	
	objects = models.Manager()

	def __str__(self):
		return self.user.username

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
