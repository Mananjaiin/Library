from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book
from .forms import BookForm
from django.db.models import Q
from django.http import JsonResponse
from django.http import JsonResponse
from django.db.models import Q
from .models import Book

def ajax_search(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    books_data = list(books.values('id', 'title', 'author', 'published_date', 'isbn'))
    return JsonResponse({'books': books_data})

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
        return Book.objects.all()

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        if request.is_ajax():
            return JsonResponse({'message': 'Book deleted successfully!'}, status=200)
        return redirect(self.success_url)