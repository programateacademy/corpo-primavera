from django.db import models
import datetime


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to ="projects_primavera/images/")
    date = models.DateField(datetime.date.today)