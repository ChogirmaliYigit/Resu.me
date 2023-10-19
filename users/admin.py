from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ('email', 'is_active', 'is_superuser', 'last_login', 'date_joined', )
    fields = ('first_name', 'last_name', 'username', 'email', 'profile_image', 'cover_image', 'bio', 'social_media_link', )
