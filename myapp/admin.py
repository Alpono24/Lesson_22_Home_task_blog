from django.contrib import admin
# from myproject.myapp.models import Product
from .models import Product, Emploees, Object, Post


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price', 'description','country','in_stock')
    list_filter = ('in_stock',)
    search_fields = ('name',)

@admin.register(Emploees)
class EmploeesAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'position','sex','age','salary','email','notes','in_stock')
    list_filter = ('in_stock',)
    search_fields = ('first_name',)


@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'street', 'position')

@admin.register(Post)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'author', 'user_id')
