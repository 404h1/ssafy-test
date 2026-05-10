from django.shortcuts import render, get_object_or_404
from .models import Author

def index(request):
    authors = Author.objects.all()
    return render(request, 'libraries/index.html', {'authors': authors})

def detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'libraries/detail.html', {'author': author})