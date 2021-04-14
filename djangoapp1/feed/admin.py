from django.contrib import admin
from .models import Post, Comments, Like, Music, Video

admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Like)
admin.site.register(Music)
admin.site.register(Video)

