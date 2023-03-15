from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombres y Apellidos')
    email = models.EmailField(max_length=254, verbose_name='Email')
    subject = models.CharField(max_length=400, verbose_name='Asunto')
    phone = PhoneNumberField(verbose_name='Teléfono (agregar el +57 o indicador de tu país)')
    country = models.CharField(max_length=100, verbose_name='País')
    message = models.TextField(verbose_name='Mensaje')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de envío')

