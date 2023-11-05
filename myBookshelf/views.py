from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm
from django.contrib import messages
from .models import Book


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Book Added successfully")
            return redirect('my_books')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})


def my_books(request):
    books = Book.objects.all()
    return render(request, 'my_books.html', {'book': books})


def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    messages.success(request, "Book Deleted successfully")
    return redirect('my_books')