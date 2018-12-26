from django.contrib import admin
from .models import Book, Author, Publish, Category, Tag

# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publish)
admin.site.register(Category)
admin.site.register(Tag)