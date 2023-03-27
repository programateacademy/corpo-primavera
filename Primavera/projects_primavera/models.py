from django.db import models
import datetime


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to ="projects_primavera/images/")
    date = models.DateField(datetime.date.today)
    def __str__(self):
        return self.title

class Activities(models.Model):
    activity = models.CharField(max_length=100)
    observation = models.TextField()
    endate = models.DateField(datetime.date.today)
    title = models.ForeignKey(Project, on_delete=models.CASCADE)
    approved  = models.BooleanField()
    pending   = models.BooleanField()
    def __str__(self):
        return self.title


