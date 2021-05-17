from django.contrib import admin
from post.models import Post, Category
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'jpublish', 'status', 'cat_to_str')
    list_filter = (('publish', JDateFieldListFilter), 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}  # autocomplete slug when type title
    ordering = ('status', '-publish')

    def cat_to_str(self, obj):
        return ','.join([category.title for category in obj.category.all()])

    cat_to_str.short_description = 'دسته بندی'
