# libraries/views.py
# 책 전체 목록을 확인 할 수 있는 페이지를 제공한다.
# 책 상세 정보를 확인 할 수 있는 페이지를 제공한다.

from django.shortcuts import render
from .models import Book

def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'libraries/index.html', context)

def detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    context = {
        'book': book,
    }
    return render(request, 'libraries/detail.html', context)