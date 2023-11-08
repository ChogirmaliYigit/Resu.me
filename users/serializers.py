from .models import *
from rest_framework import serializers

class PostSerialaizer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'user', 'title', 'slug', 'description', 'image', 'reply_to', 'created', 'updated', )
        model = Post
