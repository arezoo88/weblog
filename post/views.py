from django.shortcuts import render
from .models import Post


def home(request):
    posts = Post.objects.filter(status='p')
    context = {
        'posts': posts
    }
    return render(request, 'post/index.html', context)
