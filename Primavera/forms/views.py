from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from django.shortcuts import redirect
from django.conf import settings
from .forms import Contact_Form

def index(request):
    contact_form = Contact_Form()
    if request.method == 'POST':
        contact_form = Contact_Form(data=request.POST)

        if contact_form.is_valid():
            contact_form.save()
            return redirect(reverse('index')+'?ok')
        
        else:
            return redirect(reverse('index')+'?error')

    return render(request, 'form/index.html', {'form':contact_form})
