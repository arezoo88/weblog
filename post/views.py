from django.shortcuts import render,get_object_or_404
from .models import Post,Category


def home(request):
    posts = Post.objects.filter(status='p')
    context = {
        'posts': posts
    }
    return render(request, 'post/index.html', context)


def detail(request, slug):
    context = {
        'post': get_object_or_404(Post, slug=slug, status='p')
    }
    return render(request, 'post/detail.html', context)


def category(request, slug):
    context = {
        'category': get_object_or_404(Category, slug=slug, status=True)
    }
    return render(request, 'post/category.html', context)
