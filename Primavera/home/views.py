from django.shortcuts import render
from blog.models import Post

def index(response):
    return render(response, 'home/index.html',{})

def home(request):
    posts = Post.objects.all()[:5]