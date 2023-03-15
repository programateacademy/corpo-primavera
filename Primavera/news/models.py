from django.db import models


class New(models.Model):
    image = models.ImageField(upload_to='news/images')
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=2000)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.title)

