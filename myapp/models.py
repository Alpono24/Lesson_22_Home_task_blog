
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True) #blank=True - разрешаем что бы было пустым
    price = models.DecimalField(max_digits=10, decimal_places=2)
    country = models.CharField(max_length=30)
    in_stock = models.BooleanField(default=True)

SEX_CHOICES = [
    ('w', 'Женский'),
    ('m', 'Мужской')
]

class Emploees(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=30)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='', blank=True)
    age = models.DecimalField(max_digits=2,decimal_places=0)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField()
    notes = models.TextField(blank=True)
    in_stock = models.BooleanField(default=True)

class Object(models.Model):
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    position = models.CharField(max_length=30)

class Post(models.Model):
    title = models.CharField(max_length=100, blank=False)
    body = models.TextField(blank=False)
    author = models.CharField(max_length=100, blank=False)
    user_id = models.DecimalField(max_digits=2,decimal_places=0)
