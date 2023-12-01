from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm
from django.contrib import messages
from .models import Book
from django.db.models import Q

@login_required(login_url='login')
def my_books(request):
    q = request.GET.get('q', '')  # Get the search query from the request

    if q:
        # Filter books based on the search query
        books = Book.objects.filter(
            Q(title__icontains=q) |
            Q(author__icontains=q) |
            Q(genre__icontains=q)
        )
    else:
        # If no search query, display all books
        books = Book.objects.all()
    return render(request, 'my_books.html', {'book': books, 'search_query': q})

@login_required(login_url='login')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully!')
            return redirect('my_books')  # Redirect to the list view
    else:
        form = BookForm()

    return render(request, 'add_book.html', {'form': form})


@login_required(login_url='login')
def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('my_books')  # Redirect to the list view
    else:
        form = BookForm(instance=book)

    return render(request, 'update_book.html', {'form': form, 'book': book})


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    messages.success(request, "Book Deleted successfully")
    return redirect('my_books')


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('my_books')
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('login')

        else:
            messages.error(request, 'Username OR password does not exist')

    context = {'page': page}
    return render(request, 'login-register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('my_books')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'login-register.html', {'form': form})
