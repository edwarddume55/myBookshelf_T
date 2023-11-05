from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm
from .models import Book


def book_upload(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('my_books')

    else:
        form = BookForm()
        return render(request, 'add_book.html', {'form': form})


def my_books(request):
    books = Book.objects.all()
    return render(request, 'my_books.html', {'book': books})
