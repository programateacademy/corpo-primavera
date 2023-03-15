from django.shortcuts import render,redirect

from .models import New

def index(request):
    news = New.objects.all()
    return render(request,'news/index.html',{'news':news})

def post_news(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']
        new = New.objects.create(image = image, title = title, description = description)
        new.save()
        return redirect('news:index')
        
    return render(request, 'post_news/post.html',{})