from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from django.shortcuts import redirect
from django.conf import settings
from .forms import Contact_Form
# Create your views here.
def about(request):

    contact_form = Contact_Form()
    if request.method == 'POST':
        contact_form = Contact_Form(data=request.POST)

        if contact_form.is_valid():
            contact_form.save()
            return redirect(reverse('about')+'?ok')
        
        else:
            return redirect(reverse('about')+'?error')
    return render(request, 'home_about.html',{'form':contact_form})

