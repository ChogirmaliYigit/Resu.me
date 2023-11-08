from django.contrib import admin

from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ('email', 'is_active', 'is_superuser', 'last_login', 'date_joined', )
    fields = ('first_name', 'last_name', 'username', 'email', 'profile_image', 'cover_image', 'bio', )

class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title')
    fields = ('user', "title", "slug", "image", "description")
    prepopulated_fields = {"slug": ("title", )}
    list_filter = ('created', "updated", "title")
admin.site.register(Post, PostAdmin)