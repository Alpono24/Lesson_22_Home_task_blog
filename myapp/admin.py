from django.contrib import admin
# from myproject.myapp.models import Product
from .models import Post


@admin.register(Post)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'author')
