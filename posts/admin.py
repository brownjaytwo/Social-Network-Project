from django.contrib import admin

# Register your models here.
from posts.models import Post
from posts.models import PhotoPost
from posts.models import YoutubePost

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ('user', 'post', 'created')

	def post_info(self, obj):
		return obj.post

class PhotoPostAdmin(admin.ModelAdmin):
	list_display = ('user', 'image_post', 'caption', 'created')

class YoutubetubePostAdmin(admin.ModelAdmin):
	list_display = ('user', 'link', 'caption', 'created')




admin.site.register(Post, PostAdmin)
admin.site.register(PhotoPost, PhotoPostAdmin)
admin.site.register(YoutubePost, YoutubetubePostAdmin)