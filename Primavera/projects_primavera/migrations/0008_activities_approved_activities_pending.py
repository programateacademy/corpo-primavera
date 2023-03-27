# Generated by Django 4.1.7 on 2023-03-27 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_primavera', '0007_rename_nombreproyect_activities_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='activities',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='activities',
            name='pending',
            field=models.BooleanField(default=True),
        ),
    ]