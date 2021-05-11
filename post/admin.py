from django.contrib import admin
from post.models import Post
from django_jalali.admin.filters import JDateFieldListFilter

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'jpublish', 'status')
    list_filter = (('publish', JDateFieldListFilter), 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}  # autocomplete slug when type title
    ordering = ('status', '-publish')
