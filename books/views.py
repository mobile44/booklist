from django.shortcuts import render
from django.views.generic import (
    CreateView, 
    ListView, 
    UpdateView, 
    DetailView, 
    DeleteView
)
from books.models import Book
from django.urls import reverse_lazy

class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books"

class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "books"

class BookUpdateView(UpdateView):
    model = Book
    fields = ('title', 'user', 'status',)
    template_name = "books/book_update.html"

class BookDeleteView(DeleteView):
    model = Book
    template_name = "books/book_delete.html"
    success_url = reverse_lazy('book_list')

class BookCreateView(CreateView):
    model = Book
    fields = ('title', 'user', 'status',)
    template_name = "books/book_create.html"
    success_url = reverse_lazy('book_list')
