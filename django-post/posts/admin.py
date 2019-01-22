from django.contrib import admin

from .models import Post, Commit


# Register your models here.

admin.site.register(Post)
admin.site.register(Commit)