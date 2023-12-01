from django import forms
from .models import Book
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'summary', 'genre', 'publish_date', 'book']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
            'publish_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'book': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    class RegistrationForm(UserCreationForm):
        class Meta:
            model = User
            fields = ['username', 'password1', 'password2']

    class LoginForm(forms.Form):
        username = forms.CharField(
            label="Username",
            widget=forms.TextInput(attrs={'class': 'form-control'})
        )
        password = forms.CharField(
            label="Password",
            widget=forms.PasswordInput(attrs={'class': 'form-control'})
        )