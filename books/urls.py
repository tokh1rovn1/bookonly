from django.urls import path
from .views import BookDetailView, BookListView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail')
]