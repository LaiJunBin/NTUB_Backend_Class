from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField('書名', max_length=20)
    price = models.PositiveIntegerField('價錢')
    introduction = models.TextField('簡介')

    def __str__(self):
        return self.name