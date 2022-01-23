from django.db import models
from django.contrib.auth.models import User

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Transpose, SmartResize


# Create your models here.
class Post(models.Model):
	post = models.CharField(max_length=500)
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

class PhotoPost(models.Model):
	image = models.ImageField(upload_to='photo_post', blank=False)
	image_post = ImageSpecField(source='image', processors=[Transpose(),ResizeToFill(700, 600)], format='JPEG', options={'quality': 100})

	caption = models.CharField(max_length=500)
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


class YoutubePost(models.Model):
	link = models.CharField(max_length=50)
	caption = models.CharField(max_length=500)

	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)