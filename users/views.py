from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required

from .models import User
from .utils import get_profile_response, fetch_github_activity


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
    return get_profile_response(request, 'posts')


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
