from django.shortcuts import render, get_object_or_404,redirect
from .models import Post

def render_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts':posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render (request, 'post_detail.html', {"post": post} )

def posting(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']
        date = request.POST['date']
        new = Post.objects.create(image = image, title = title, description = description, date = date)
        new.save()
        return redirect('blog:posts')
    return render(request, 'post_posting/posting.html',{})