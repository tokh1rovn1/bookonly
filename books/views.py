from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Category

# Create your views here.

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        # URL'dan category_id ni olish (masalan: ?category=1)
        category_id = self.request.GET.get('category')
        if category_id:
            # Agar category_id bo'lsa, kitoblarni filtrlaymiz
            return Book.objects.filter(category_id=category_id)
        # Agar category_id bo'lmasa, hamma kitoblarni chiqaramiz
        return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        # Tanlangan kategoriyani belgilab qo'yish uchun (optional)
        context['current_category'] = self.request.GET.get('category')
        return context
    

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'
    pk_url_kwarg = 'pk'
