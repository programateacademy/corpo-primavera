# Generated by Django 4.1.7 on 2023-03-27 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_primavera', '0008_activities_approved_activities_pending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activities',
            name='approved',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='activities',
            name='pending',
            field=models.BooleanField(),
        ),
    ]
