from django.shortcuts import render

# Create your views here.

from django.views.generic.base import View

from .models import Book


class BooksView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, "book/book_list.html", {"book_list": books})

class BookDetailView(View):
    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        return render(request, "book/book_detail.html", {"book": book})