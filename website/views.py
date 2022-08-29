from django.shortcuts import render
from .models import Post


def home(request):
    posts_list = Post.objects.all()
    data = {'posts': posts_list}
    return render(request, 'index.html', data)


def post_detail(request, id):
    post = Post.objects.get(id=id)
    data = {'post': post}
    return render(request, 'post_detail.html', data)
