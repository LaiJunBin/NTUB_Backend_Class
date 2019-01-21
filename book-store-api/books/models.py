from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField('書名', max_length=50)
    price = models.PositiveIntegerField('價格')

    def __str__(self):
        return self.name