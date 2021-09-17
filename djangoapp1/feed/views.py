from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .forms import NewCommentForm, NewPostForm, MusicForm, VideoForm, MusicUpdateForm
from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comments, Like, Music, Video
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import json
from json import dumps
from rest_framework import viewsets
from .serializers import MusicSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.core.exceptions import ValidationError	

MUSIC_FILE_TYPES = ['mp3']




class PostListView(ListView):
    model = Post
    template_name = 'feed/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            liked = [i for i in Post.objects.all() if Like.objects.filter(user = self.request.user, post=i)]
            context['liked_post'] = liked
        return context
    


class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'feed/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(UserPostListView, self).get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        liked = [i for i in Post.objects.filter(user_name=user) if Like.objects.filter(user = self.request.user, post=i)]
        context['liked_post'] = liked
        return context
        
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(user_name=user).order_by('-date_posted')


@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user
    is_liked =  Like.objects.filter(user=user, post=post)
    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.post = post
            data.username = user
            data.save()
            return redirect('post-detail', pk=pk)
    else:
        form = NewCommentForm()
    return render(request, 'feed/post_detail.html', {'post':post, 'is_liked':is_liked, 'form':form})

@login_required
def create_post(request, slug):
    user = request.user
    if request.method == "POST":
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_name = user
            data.save()
            messages.success(request, f'Posted Successfully')
            return redirect('home')
    else:	
        form = NewPostForm()
    return render(request, 'feed/create_post.html', {'form':form})

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['description', 'pic', 'tags']
    template_name = 'feed/create_post.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)
        

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user_name:
            return True
        return False
        
        

@login_required
def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.user== post.user_name:
        Post.objects.get(pk=pk).delete()
        messages.error(request, f'Post Deleted')
    return redirect('home')

@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comments, pk=pk)
    if request.user.id == comment.username_id:
        Comments.objects.get(pk=pk).delete()
        messages.error(request, f'Comment Deleted')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def search_posts(request):
    query = request.GET.get('p')
    object_list = Post.objects.filter(tags__icontains=query).order_by('-date_posted')
    liked = [i for i in object_list if Like.objects.filter(user = request.user, post=i)]
    context ={
        'posts': object_list,
        'liked_post': liked
    }
    return render(request, "feed/search_posts.html", context)

@login_required
def like(request):
    post_id = request.GET.get("likeId", "")
    user = request.user
    post = Post.objects.get(pk=post_id)
    liked= False
    like = Like.objects.filter(user=user, post=post)
    if like:
        like.delete()
    else:
        liked = True
        Like.objects.create(user=user, post=post)
    resp = {
        'liked':liked
    }
    response = json.dumps(resp)
    return HttpResponse(response, content_type = "application/json")


@login_required 
def music_upload(request, slug):
    if request.method == "POST":
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.artist = request.user
            song.track = request.FILES['track']
            file_type = song.track.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in MUSIC_FILE_TYPES:
                messages.error(request, f'ERROR - Track needs to be in MP3 format, Please try again!')
                return render(request, 'feed/music_upload.html', {'form':form})
            else:
                song.save()
                messages.success(request, f'Track Uploaded')
                return redirect('my_profile', slug=slug)
    else:
        form = MusicForm()
    return render(request, 'feed/music_upload.html', {'form':form})


@login_required
def edit_tracks(request, slug):
    p = request.user.profile
    you = p.user
    music = Music.objects.all().filter(artist=you).order_by('-date_posted')
    context={
        'u': you,
        'music': music,
        }
    return render(request, 'feed/edit_tracks.html', context)

@login_required
def edit_song(request, pk, slug):
    track = Music.objects.get(pk=pk)
    if request.method == 'POST':
            m_form = MusicUpdateForm(request.POST, request.FILES, instance=track)
            if m_form.is_valid():
                    m_form.save()
                    messages.info(request, f'Track updated!')
                    return redirect('my_profile', slug=slug)
            
    else:
            m_form = MusicUpdateForm(instance=track)
    context ={
            'm_form': m_form,
    }
    return render(request, 'feed/music_update.html', context)


@login_required
def track_delete(request, pk):
    track = get_object_or_404(Music, pk=pk)
    if request.user.id == track.artist_id:
        Music.objects.get(pk=pk).delete()
        messages.error(request, f'Track deleted')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def video_upload(request, slug):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.videoUser= request.user
            video.save()  
            messages.success(request, f'Video Uploaded')
            return redirect('my_profile', slug=slug)
    else:
        form = VideoForm()
    return render(request, 'feed/video_upload.html', {'form':form})


@login_required
def edit_videos(request, slug):
    p = request.user.profile
    you = p.user
    video = Video.objects.all().filter(videoUser_id=you)
    context={
        'u': you,
        'video': video,
        }
    return render(request, 'feed/edit_videos.html', context)


@login_required
def video_delete(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.user.id == video.videoUser_id:
        Video.objects.get(pk=pk).delete()
        messages.error(request, f'Video Deleted')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))    



class MusicViewSet(viewsets.ModelViewSet):

    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['artist']


    def get_queryset(self):
        user = self.request.user
        songs = Music.objects.all().filter(artist=user).order_by('-date_posted')
        return songs




    