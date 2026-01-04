from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Kategoriyalar'

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name_plural = 'Mualiflar'


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    descriptions = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to='media/', blank=True, null=True)
    created_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.author}"
    
    class Meta:
        verbose_name_plural = 'kitoblar'