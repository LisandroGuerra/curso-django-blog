from django.shortcuts import render
from .models import Post, Contact


def home(request):
    posts_list = Post.objects.all()
    data = {'posts': posts_list}
    return render(request, 'index.html', data)


def post_detail(request, id):
    post = Post.objects.get(id=id)
    data = {'post': post}
    return render(request, 'post_detail.html', data)


def save_form(request):
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']

    Contact.objects.create(
        name=name,
        email=email,
        message=message
    )
    return render(request, 'contact_saved.html', {'contact_name': name})
