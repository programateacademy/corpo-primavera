from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from django.shortcuts import redirect
from django.conf import settings
from .forms import Contact_Form
from blog.models import Post

def index(response):

    contact_form = Contact_Form()
    if response.method == 'POST':
        contact_form = Contact_Form(data=response.POST)

        if contact_form.is_valid():
            contact_form.save()
            return redirect(reverse('home:index')+'?ok')
        
        else:
            return redirect(reverse('home:index')+'?error')
    return render(response, 'home/index.html',{'form':contact_form})

def home(request):
    posts = Post.objects.all()[:5]