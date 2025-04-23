from django.contrib import admin
from .models import Category, NewsPost, Comment

admin.site.register(Category)
admin.site.register(NewsPost)
admin.site.register(Comment)
