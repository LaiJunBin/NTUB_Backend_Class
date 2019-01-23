from django.contrib import admin

from .models import Post, Commit


admin.site.register(Post)
admin.site.register(Commit)
