from django.contrib import admin
from .models import Category, Author, Book

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']
    list_filter = ['name']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'bio', 'birth_date']
    search_fields =['name']
    list_filter = ['birth_date']
    readonly_fields = ['bio']


class CategoryInline(admin.TabularInline):
    model = Book.category.field.model
    extra = 1

class AuthorInline(admin.TabularInline):
    model = Book.author.field.model
    extra = 1

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'author','price', 'category', ]
    search_fields = ['title', 'author__name',]
    readonly_fields = ['created_add']
    #inlines = [AuthorInline, CategoryInline]
    list_per_page = 10
    

