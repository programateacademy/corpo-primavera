from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('Accounts:login')
    else:
        form = RegisterForm()
    
    return render(response, 'Register/index.html', {'form':form})

def loginPage(request):
    return render(request, 'registration/login.html',{})



def logoutPage(request):
    return render(request, 'exit/logout.html',{})
