from django.contrib import admin
from django.urls import path, include
from . import views
from .views import PostUpdateView, PostListView, UserPostListView, MusicViewSet
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'music_all', views.MusicViewSet, 'music_all')
# router.register(r'tracks', views.TrackViewSet, 'tracks')

urlpatterns=[
	path('music/', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	path('', PostListView.as_view(), name='home'),
	path('post/new/<slug:slug>/', views.create_post, name='post-create'),
	path('post/<int:pk>/', views.post_detail, name='post-detail'),
	path('like/', views.like, name='post-like'),
	path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
	path('post/<int:pk>/delete/', views.post_delete, name='post-delete'),
	path('search_posts/', views.search_posts, name='search_posts'),
	path('user_posts/<str:username>/', UserPostListView.as_view(), name='user-posts'),
	path('comments/<int:pk>/delete/', views.comment_delete, name='comment-delete'),
	path('music/new/<slug:slug>/', views.music_upload, name='music-upload'),
	path('edit-tracks/<slug:slug>/', views.edit_tracks, name='edit_tracks'),
	path('edit/<int:pk>/song/<slug:slug>/', views.edit_song, name='edit-song'),
	path('track/<int:pk>/delete/', views.track_delete, name='track-delete'),
	path('video/new/<slug:slug>/', views.video_upload, name='video-upload'),
	path('edit-videos/<slug:slug>/', views.edit_videos, name='edit_videos'),
	path('video/<int:pk>/delete/', views.video_delete, name='video-delete'),
]
