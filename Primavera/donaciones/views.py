from django.shortcuts import render,redirect
from django.urls import reverse
from django.shortcuts import redirect
from .forms import Contact_Form
# Create your views here.
def donaciones(response):

    contact_form = Contact_Form()
    if response.method == 'POST':
        contact_form = Contact_Form(data=response.POST)

        if contact_form.is_valid():
            contact_form.save()
            return redirect(reverse('donaciones:donaciones')+'?ok')
        
        else:
            return redirect(reverse('donaciones:donaciones')+'?error')
    return render(response,'donaciones.html',{'form':contact_form})