from django.urls import path, include

from .views import index, profile, resume, posts, work, activity, logout


urlpatterns = [
    path('', index, name='index'),
    path('profile/', include([
        path('', profile, name='profile'),
        path('resume', resume, name='resume'),
        path('posts', posts, name='posts'),
        path('work', work, name='work'),
        path('activity', activity, name='activity'),
    ])),
    path('logout', logout, name='logout'),
]
