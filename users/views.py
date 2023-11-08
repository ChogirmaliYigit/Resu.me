from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required

from .models import User, Post
from .utils import get_profile_response, fetch_github_activity
from django.views import View

from rest_framework import generics
from .serializers import *
from rest_framework.permissions import * 

def index(request):
    if request.user.is_authenticated:
        return render(request, 'authorized_index.html', {'user': request.user})
    return render(request, 'unauthorized_index.html')


@login_required
def profile(request):
    return get_profile_response(request)


@login_required
def resume(request):
    return get_profile_response(request, 'resume')


@login_required
def posts(request):
    posts = Post.objects.all()

    return get_profile_response(request, 'posts', {'posts': posts})


@login_required
def work(request):
    return get_profile_response(request, 'work')


@login_required
def activity(request):
    github_activity = fetch_github_activity('ChogirmaliYigit')
    return get_profile_response(request, 'activity', {'github_activity': github_activity})


@login_required
def logout(request):
    django_logout(request)
    return redirect('index')

class BlogList(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, "templates/posts.html", {"posts": posts})

    # def post(self, request):
    #     post = get_object_or_404(Post)
    #     title = request.POST.get('title')
    #     description = request.POST.get('description')
    #     image = request.POST.get('image')
    #     reply_to = request.POST.get('reply_to')
    #     Post.objects.create(title=title, description=description, image=image, reply_to=reply_to, post=post)


class BlogDetail(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        return render(request, 'templates/posts.html', {"post": post})
    
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        user = request.POST.get('user')
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.POST.get('image')
        reply_to = request.POST.get('reply_to')
        Post.objects.create(user=request.user, title=title, description=description, image=image, reply_to=reply_to, post=post)
        return redirect('detail', slug)

# CRUD -----------------> POSTS
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialaizer
    permission_classes = [IsAuthenticated]

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialaizer
    permission_classes = [IsAuthenticated]