from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    content = models.TextField('內文')
    creator = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='建立者')
    create_at = models.DateTimeField('建立時間', auto_now_add=True)
    update_at = models.DateTimeField('更新時間', auto_now=True)
    def __str__(self):
        return 'Post create by {}'.format(self.creator.username)