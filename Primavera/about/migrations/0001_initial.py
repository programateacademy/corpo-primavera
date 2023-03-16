# Generated by Django 4.1.6 on 2023-03-16 17:12

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombres y Apellidos')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('subject', models.CharField(max_length=400, verbose_name='Asunto')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Teléfono (agregar el +57 o indicador de tu país)')),
                ('country', models.CharField(max_length=100, verbose_name='País')),
                ('message', models.TextField(verbose_name='Mensaje')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de envío')),
            ],
        ),
    ]