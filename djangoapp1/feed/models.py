from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from users.models import Profile
from embed_video.fields import EmbedVideoField
from .validators import file_size



class Post(models.Model):
	description = models.TextField(max_length=255)
	pic = models.ImageField(upload_to='path/to/img', blank=True)
	date_posted = models.DateTimeField(default=timezone.now)
	user_name = models.ForeignKey(User, on_delete=models.CASCADE)
	tags = models.CharField(max_length=100, blank=True)

	def __str__(self): 
		return self.description

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})
 

class Comments(models.Model):
	post = models.ForeignKey(Post, related_name='details', on_delete=models.CASCADE)
	username = models.ForeignKey(User, related_name='details', on_delete=models.CASCADE)
	comment = models.CharField(max_length=255)
	comment_date = models.DateTimeField(default=timezone.now)

class Like(models.Model):
	user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
	post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)


class Music(models.Model):
	track = models.FileField(upload_to='path/to/audio', validators=[file_size])
	title = models.TextField(max_length=50)
	artwork = models.ImageField(upload_to='path/to/img', validators=[file_size])
	artist_name = models.TextField(max_length=50)
	artist = models.ForeignKey(User, on_delete=models.CASCADE)
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title


	

class Video(models.Model):
	video = EmbedVideoField()
	caption = models.TextField(max_length=30)
	videoUser = models.ForeignKey(User, on_delete=models.CASCADE, default='') 
	date_posted = models.DateTimeField(default=timezone.now)





	





