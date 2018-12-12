from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    introduction = models.TextField()

    def __str__(self):
        return self.name