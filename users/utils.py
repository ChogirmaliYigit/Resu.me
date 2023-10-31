import requests

from django.shortcuts import render


def get_profile_response(request, page='', extra_context=None):
    context = {'user': request.user, 'page': page}
    if extra_context:
        context.update(extra_context)
    return render(request, 'profile.html', context)


def fetch_github_activity(username):
    url = f'https://api.github.com/users/{username}/events/public'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
