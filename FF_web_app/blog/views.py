from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse1


# Create your views here.

'''
posts = [
    {
        'author': 'Naim',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'September 23, 2018'
    },
    {
        'author': 'Shawon',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'September 24, 2018'
    }
]
'''

def home(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/home.html', context)


def about(request):
    # return HttpResponse('<h1>Blog about </h1>')
    # We use HttpResponse if we do not use rendering
    return render(request, 'blog/about.html', {'title': 'about'})
