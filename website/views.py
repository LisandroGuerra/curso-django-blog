from django.shortcuts import render

from .models import Post


def hello_website(request):
    posts_list = Post.objects.all()
    data = {'posts': posts_list}
    return render(request, 'index.html', data)
