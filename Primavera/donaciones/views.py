from django.shortcuts import render

# Create your views here.
def donaciones(response):
    return render(response,'donaciones.html',{})