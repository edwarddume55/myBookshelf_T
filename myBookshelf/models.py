from django import forms
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    isbn = models.CharField(max_length=10)
    summary = models.TextField()
    genre = models.CharField(max_length=10)
    publish_date = models.DateTimeField()
    book = models.ImageField(upload_to='books/')

