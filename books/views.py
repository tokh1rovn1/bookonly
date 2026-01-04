from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Category

# Create your views here.

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'
    pk_url_kwarg = 'pk'
