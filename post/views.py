from django.shortcuts import render,get_object_or_404
from .models import Post,Category
from django.core.paginator import Paginator

def home(request):
    posts = Post.objects.published()
    paginator = Paginator(posts, 2) # Show 2 posts per page.
    # context = {
    #     'posts': posts
    # }
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'post/index.html', {'posts':posts})


def detail(request, slug):
    context = {
        'post': get_object_or_404(Post.objects.published(), slug=slug, status='p')
    }
    return render(request, 'post/detail.html', context)


def category(request, slug):
    category = get_object_or_404(Category, slug=slug, status=True)
    posts = category.posts.published()
    paginator = Paginator(posts, 2) # Show 2 posts per page.
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'post/category.html', context)
