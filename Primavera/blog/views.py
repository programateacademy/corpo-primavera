from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Post
from datetime import datetime

def render_posts(request):
    posts = Post.objects.filter(date__lte=datetime.now()).order_by('-date')
    return render(request, 'posts.html', {'posts':posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render (request, 'post_detail.html', {"post": post} )

@permission_required('blog.add_post')
def posting(request):
    posting = Post.objects.all().order_by('-date')
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']
        date = request.POST['date']
        new = Post.objects.create(image = image, title = title, description = description, date = date)
        new.save()
        return redirect('blog:posts')
    return render(request, 'post_posting/posting.html',{})
