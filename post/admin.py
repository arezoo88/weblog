from django.contrib import admin
from post.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
